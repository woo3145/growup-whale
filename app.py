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
from services import loginService

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
    starttime = db.Column(db.String(10000), nullable=False)
 
#     whale_id = db.Column(db.Integer, db.ForeignKey("whale.id"))
#     whale = relationship("whale", back_populates="user")
#     study_type_level_id = db.Column(
#         db.Integer, db.ForeignKey("studytypelevel.id"))
#     study_type_level = relationship("studytypelevel", back_populates="user")

<<<<<<< refs/remotes/upstream/main
=======
    # whale_id = db.Column(db.Integer, db.ForeignKey("whale.id"))
    # whale = relationship("whale", back_populates="user")
    # study_type_level_id = db.Column(
    #     db.Integer, db.ForeignKey("studytypelevel.id"))
    # study_type_level = relationship("studytypelevel", back_populates="user")
>>>>>>> fix loginService app.py

# class Whale(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     level = db.Column(db.String(100), nullable=False)
#     job = db.Column(db.String(100), nullable=False)
#     exp = db.Column(db.String(100), nullable=False)

<<<<<<< refs/remotes/upstream/main
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

=======
# class Whale(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     level = db.Column(db.String(100), nullable=False)
#     job = db.Column(db.String(100), nullable=False)
#     exp = db.Column(db.String(100), nullable=False)

#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
>>>>>>> fix loginService app.py

# class Studytypelevel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     blog_lv = db.Column(db.String(100), nullable=False)
#     argorithm_lv = db.Column(db.String(100), nullable=False)
#     main_lv = db.Column(db.String(100), nullable=False)
#     cs_lv = db.Column(db.String(100), nullable=False)

<<<<<<< refs/remotes/upstream/main
=======
# class Studytypelevel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     blog_lv = db.Column(db.String(100), nullable=False)
#     argorithm_lv = db.Column(db.String(100), nullable=False)
#     main_lv = db.Column(db.String(100), nullable=False)
#     cs_lv = db.Column(db.String(100), nullable=False)

>>>>>>> fix loginService app.py
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


with app.app_context():
<<<<<<< refs/remotes/upstream/main
    # 데이터베이스에 추가하기 전에 비밀번호를 bcrypt로 해시화 dddd
    db.create_all() 
=======
    db.drop_all()
    db.create_all()
    # 데이터베이스에 추가하기 전에 비밀번호를 bcrypt로 해시화
    hashed_password = bcrypt.generate_password_hash('test1234').decode('utf-8')

    # User 객체 생성 및 데이터베이스에 추가
    new_user = User(email='test@test.com', password=hashed_password, nickname='TestUser', starttime='2023-01-01')
    db.session.add(new_user)
    db.session.commit()
>>>>>>> fix loginService app.py

@app.route("/")
def home():
    return render_template('main.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
<<<<<<< refs/remotes/upstream/main
<<<<<<< refs/remotes/upstream/main
=======
>>>>>>> fix loginService app.py
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
<<<<<<< refs/remotes/upstream/main
            response = make_response(login_result)
=======
            response = make_response(render_template('login.html', login_result=login_result))
>>>>>>> fix loginService app.py
            response.set_cookie('access_token', access_token, httponly=True, secure=True)

            return response

        else:
<<<<<<< refs/remotes/upstream/main
            return make_response(login_result)
=======
            return render_template('login.html', login_result=login_result)
>>>>>>> fix loginService app.py

    else:
        return jsonify(message='Method not allowed'), 405

<<<<<<< refs/remotes/upstream/main
=======
    
    return render_template('login.html')
>>>>>>> feat add login.html
=======
>>>>>>> fix loginService app.py

@app.route("/register")
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
