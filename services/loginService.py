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
