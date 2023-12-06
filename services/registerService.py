

def register(User, db, email, password, nickname, password_check):
    if User.query.filter_by(email=email).first():
        return {'Success': False, 'message': "중복된 이메일입니다"}
    elif not (email and password and nickname):
        return {'Success': False, 'message': "입력되지 않은 정보가 있습니다"}
    elif password != password_check:
        return {'Success': False, "message": "비밀번호가 일치하지 않습니다"}

    user = User(nickname, email, password)
    db.session.add(user)
    db.session.commit()
    return {'Success': True, 'message': "요청에 성공했습니다"}
