<<<<<<< refs/remotes/upstream/main
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
=======
from flask_bcrypt import check_password_hash, generate_password_hash, Bcrypt
from flask_jwt_extended import create_access_token
bcrypt = Bcrypt()
>>>>>>> fix loginService app.py

def login(db, user_class, email, password):
    # User 클래스를 사용하여 로그인 로직 구현
    user = db.session.query(user_class).filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        # 비밀번호가 일치하면 JWT 토큰 생성
        access_token = create_access_token(identity=email)
        return {'success': True, 'access_token': access_token}
    else:
<<<<<<< refs/remotes/upstream/main
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
=======
        return {'success': False, 'message': 'Invalid email or password'}
>>>>>>> fix loginService app.py
