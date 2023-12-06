<<<<<<< refs/remotes/upstream/main
<<<<<<< refs/remotes/upstream/main
from flask_bcrypt import check_password_hash, generate_password_hash, Bcrypt
from flask_jwt_extended import create_access_token
bcrypt = Bcrypt()

def login(db, user_class, email, password):
    # User 클래스를 사용하여 로그인 로직 구현
    user = db.session.query(user_class).filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        # 비밀번호가 일치하면 JWT 토큰 생성
        access_token = create_access_token(identity=email)
        return {'success': True, 'access_token': access_token}
    else:
        return {'success': False, 'message': 'Invalid email or password'}
=======
from flask import Flask, jsonify, request, SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, Bcrypt
import os
import secrets
=======
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy  # 변경된 부분
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
>>>>>>> feat add login.html

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # SQLite 데이터베이스 파일 설정
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 추적 기능 비활성화
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# 사용자 데이터베이스 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

# Flask-JWT-Extended 설정
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# 로그인 엔드포인트

def login(email):
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # 사용자가 존재하고 비밀번호가 일치하면 JWT 토큰을 생성
    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid email or password'), 401

# 보호된 리소스에 접근하기 위한 엔드포인트
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # 현재 로그인한 사용자 식별자 가져오기
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
<<<<<<< refs/remotes/upstream/main
    app.run(debug=True)

>>>>>>> add loginservice
=======
    app.run(debug=True)
>>>>>>> feat add login.html
