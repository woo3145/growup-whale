# 필수 라이브러리
'''
0. Flask : 웹서버를 시작할 수 있는 기능. app이라는 이름으로 플라스크를 시작한다
1. render_template : html파일을 가져와서 보여준다
'''
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import secrets
from services import loginService, registerService, dataService, jwtService

app = Flask(__name__)

# DB

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')


# JWT_SECRET_KEY가 이미 설정되어 있는지 확인
jwt_secret_key = os.environ.get('JWT_SECRET_KEY')

# JWT_SECRET_KEY가 없으면 새로운 키 생성
if jwt_secret_key is None:
    jwt_secret_key = secrets.token_hex(32)
    os.environ['JWT_SECRET_KEY'] = jwt_secret_key
    print(f"New JWT_SECRET_KEY generated: {jwt_secret_key}")

# Flask-JWT-Extended 설정
app.config['JWT_SECRET_KEY'] = jwt_secret_key
jwt = JWTManager(app)


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(100), nullable=False)
    starttime = db.Column(db.Time, nullable=True)

    whale_id = db.Column(Integer, db.ForeignKey("whale.id"))
    whale = db.relationship("Whale",  back_populates="user")

    study_type_level_id = db.Column(
        Integer, db.ForeignKey("studytypelevel.id"))
    study_type_level = db.relationship("Studytypelevel", back_populates="user")


class Whale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer, nullable=False)
    job = db.Column(db.String(100), nullable=True)
    exp = db.Column(db.Integer, nullable=True)

    user = db.relationship("User", back_populates="whale", uselist=False)


class Studytypelevel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_lv = db.Column(db.Integer, nullable=True)
    argorithm_lv = db.Column(db.Integer, nullable=True)
    main_lv = db.Column(db.Integer, nullable=True)
    cs_lv = db.Column(db.Integer, nullable=True)

    user = db.relationship(
        "User", back_populates="study_type_level", uselist=False)


with app.app_context():
    db.create_all()


@app.route("/")
@jwt_required(optional=True)
def home():
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

    percent =  (curExp / nextRequiredExp)*100
    
    curWhale = {}   
    if user_level == "1":
        curWhale = whaleData[user_level]
    else:
        curWhale = whaleData[user_level][user.whale.job][0]

    return render_template('main.html', user=user, whale=curWhale, percent=percent)
    

@app.route("/signin")
def renderSiginin():
    return render_template("signin.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')  # 리디렉션 대신 템플릿을 렌더링

    elif request.method == 'POST':
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
            response.set_cookie('access_token', access_token, httponly=True, secure=True)

            return response

        else:
            return make_response(login_result)

    else:
        return jsonify(message='Method not allowed'), 405


@app.route("/register", methods=['POST', 'GET'])
def register():

    
    if request.method == 'POST':
        data = request.get_json(silent=True)
        nickname = data.get('nickname')
        email = data.get('email')
        password = data.get('pw')
        password_check = data.get('pw_check')

        res = registerService.register(db, email, password, nickname, password_check, User,Whale,Studytypelevel)
        
        return make_response(res)

@app.route("/study")
def study():
    studyType = request.args.get("study_type")
    print(studyType)

    return redirect("/")


@app.route("/logout")
def logout():
    response = make_response(redirect("/"))
    response.delete_cookie("access_token", "", httponly=True, secure=True)
    return response

if __name__ == "__main__":
    app.run(debug=True)
