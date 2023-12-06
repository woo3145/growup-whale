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

app = Flask(__name__)

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

# 간단한 사용자 데이터베이스 역할을 하는 변수
users = {
    'user1': {'password': 'password1'},
    'user2': {'password': 'password2'}
}

# 로그인 엔드포인트
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # 사용자가 존재하고 비밀번호가 일치하면 JWT 토큰을 생성
    user = User.query.filter_by(email=email).first()

    if user and Bcrypt.check_password_hash(user.password, password):
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
    app.run(debug=True)

>>>>>>> add loginservice
