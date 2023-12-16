import os
from flask import Flask, render_template, request, redirect, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, jwt_required
import secrets
from services import loginService, registerService, dataService, jwtService, studyService
from datetime import timedelta


app = Flask(__name__)

# DB

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')


# JWT_SECRET_KEY가 이미 설정되어 있는지 확인
jwt_secret_key = os.environ.get('JWT_SECRET_KEY')
jwt_expired = timedelta(days=120)

# JWT_SECRET_KEY가 없으면 새로운 키 생성
if jwt_secret_key is None:
    jwt_secret_key = secrets.token_hex(32)
    os.environ['JWT_SECRET_KEY'] = jwt_secret_key
    print(f"New JWT_SECRET_KEY generated: {jwt_secret_key}")

# Flask-JWT-Extended 설정 
app.config['JWT_SECRET_KEY'] = jwt_secret_key
jwt = JWTManager(app)


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(100), nullable=False)
    starttime = db.Column(db.DateTime, nullable=True)

    whale_id = db.Column(db.Integer, db.ForeignKey("whale.id"))
    whale = db.relationship("whale", back_populates="user")
    study_type_level_id = db.Column(
        db.Integer, db.ForeignKey("studytypelevel.id"))
    study_type_level = db.relationship("studytypelevel", back_populates="user")


class Whale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer, nullable=False)
    job = db.Column(db.String(100), nullable=True)
    exp = db.Column(db.Integer, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Studytypelevel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_lv = db.Column(db.Integer, nullable=True)
    argorithm_lv = db.Column(db.Integer, nullable=True)
    main_lv = db.Column(db.Integer, nullable=True)
    cs_lv = db.Column(db.Integer, nullable=True)
    workout_lv = db.Column(db.Integer, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship(
        "User", back_populates="study_type_level", uselist=False)

with app.app_context():
    db.create_all()

@app.route("/")
@jwt_required(optional=True)
def home():
    current_url = request.url
    cookie = request.cookies.get("access_token")
    if not cookie:
        return redirect("/signin")
    
    user_email = jwtService.get_email_from_cookie(cookie)
    
    if not user_email:
        return redirect("/signin")

    user = db.session.query(User).filter_by(email=user_email).first()
    

    whaleData = dataService.loadWhaleData(app)

    user_level = str(user.whale.level)

    curExp = user.whale.exp
    requiredExpTable = dataService.loadRequiredExp(app)
    nextRequiredExp = requiredExpTable[user_level]

    bit = 0

    for i in range(1, int(user_level)):
        bit += requiredExpTable[str(i)]

    percent =  ((curExp - bit) / (nextRequiredExp - bit))*100
    
    curWhale = {}
    if user_level == "1":
        curWhale = whaleData[user_level]
    else:
        curWhale = whaleData[user_level][user.whale.job][0]

    isTodayStudy = False

    if user.starttime and user.starttime.date() == studyService.get_time():
        isTodayStudy = True
    
    return render_template('main.html', user=user, whale=curWhale, percent=percent, isTodayStudy=isTodayStudy, current_url=current_url)
    

@app.route("/signin")
def renderSiginin():
    cookie = request.cookies.get("access_token")
    email = jwtService.get_email_from_cookie(cookie)
    if email :
        return redirect("/")
    else:
        return render_template("signin.html")

@app.route("/login", methods=['POST'])
@app.route("/login", methods=['POST'])
def login():
    if request.method != "POST":
        return jsonify(message='Method not allowed'), 405

    data = request.get_json()
    user_email = data.get('email')
    password = data.get('password')

    # loginService의 login 함수 호출, db 전달
    login_result = loginService.login(db, User, user_email, password)

    if login_result['success']:
        # 토큰 생성
        access_token = login_result['access_token']

        # 리디렉션 대신 쿠키에 토큰 저장하고 메인 페이지로 리디렉션
        response = make_response(login_result)
        response.set_cookie('access_token', access_token, httponly=True, secure=True, max_age=jwt_expired)

        return response

    else:
        return make_response(login_result)

        
@app.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        nickname = data.get('nickname')
        email = data.get('email')
        password = data.get('pw')

        res = registerService.register(db, email, password, nickname, User,Whale,Studytypelevel)
        print(res)
        return make_response(res)


@app.route("/study")
def study():

    # email 받아오기
    cookie = request.cookies.get("access_token")
    if not cookie:
        return redirect("/signin")
    
    user_email = jwtService.get_email_from_cookie(cookie)
    
    if not user_email:
        return redirect("/signin")

    # 유저의 id 받아오기
    user = db.session.query(User).filter_by(email=user_email).first()

    # 스터디 타입 받아오기
    studyType = request.args.get("study_type")

    # 레벨별 경험치 담은 변수 생성
    nextRequiredExp = dataService.loadRequiredExp(app)[str(user.whale.level)]

    # studycheck함수로 넘겨줌
    studyService.studyCheck(db, User, nextRequiredExp, studyType, user_email)
    
    return redirect("/")



@app.route("/logout")
def logout():
    response = make_response(redirect("/"))
    response.delete_cookie("access_token", "", httponly=True, secure=True)
    return response

if __name__ == "__main__":
    app.run(debug=True)
