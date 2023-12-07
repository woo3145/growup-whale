from flask_bcrypt import generate_password_hash, Bcrypt
bcrypt = Bcrypt()

def register(db, email, password, nickname, password_check, user_class, whale_class, study_class):
    # if db.session.query(User).filter_by(email=email).first():
    #     return {'Success': False, 'message': "중복된 이메일입니다"}
    # elif not (email and password and nickname):
    #     return {'Success': False, 'message': "입력되지 않은 정보가 있습니다"}
    # elif password != password_check:
    #     return {'Success': False, "message": "비밀번호가 일치하지 않습니다"}
    
    
   try:
        new_whale = whale_class(level=1)
        new_studytypelevel = study_class()

        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        hashed_pw_check = bcrypt.generate_password_hash(password_check).decode('utf-8')

        user = user_class(
            email=email, 
            password=hashed_pw, 
            nickname=nickname, 
            starttime=None, 
            whale=new_whale,
            study_type_level=new_studytypelevel
        )

        if db.session.query(user_class).filter_by(email=user.email).first():
            return {'Success': False, 'message': "중복된 이메일입니다"}
        # elif password != password_check:
        #     return {'Success': False, "message": "비밀번호가 일치하지 않습니다"}

        # if user and bcrypt.check_password_hash(user.password, password):
        #     return {'success': True}
        
        db.session.add(user)
        db.session.commit()
        return {'success': True, 'message': "요청에 성공했습니다"}
   except:
       return {'success': False, 'message': "요청에 실패했습니다"}
