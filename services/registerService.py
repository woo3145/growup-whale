from flask_bcrypt import generate_password_hash, Bcrypt
bcrypt = Bcrypt()

def register(db, email, password, nickname, password_check, user_class, whale_class, study_class):
    
   try:
        new_whale = whale_class(level=1)
        # new_studytypelevel = study_class()
        new_studytypelevel = study_class(blog_lv=0, argorithm_lv=0, main_lv=0, cs_lv=0)

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
        
        db.session.add(user)
        db.session.commit()
        return {'success': True, 'message': "요청에 성공했습니다"}
   except:
       return {'success': False, 'message': "요청에 실패했습니다"}
