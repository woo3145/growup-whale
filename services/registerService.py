

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

        user = user_class(
            email=email, 
            password=password, 
            nickname=nickname, 
            starttime=None, 
            whale=new_whale, 
            study_type_level=new_studytypelevel
        )   
        
        db.session.add(user)
        db.session.commit()
        return {'success': True, 'message': "요청에 성공했습니다"}
   except:
       return {'success': False, 'message': "요청에 실패했습니다"}
