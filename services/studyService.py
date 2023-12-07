import datetime

# 레벨 구하기
def get_level(required_exp, total_exp) :
    level = 0
    if total_exp >= 99 : level = 5
    elif total_exp >= required_exp['4'] and total_exp < 99 : level = 4
    elif total_exp >= required_exp['3'] and total_exp < required_exp['4'] : level = 3
    elif total_exp >= required_exp['2'] and total_exp < required_exp['3'] : level = 2
    elif total_exp < required_exp['2'] : level = 1
    return level

def get_time() :
    time_str = get_time()
    time = datetime.strptime(time_str, "%Y-%m-%d")
    return time


def studyCheck(db, User, Whale, Studytypelevel, required_exp, studyType, user_email) :
    print(required_exp)

    # 유저 이메일 받아오기, id 구하기
    email = user_email
    user_list = db.session.query(User).filter_by(email=email).first()
    user_id = user_list.id


    # 한 번만 클릭 할 수 있도록 제어
    user_date = user_list.starttime
    pre_time = get_time()

    if pre_time != user_date :

        # 오늘 날짜 기록
        user_list.starttime = user_date

        # 클릭한 버튼 찾아내기
        study_type = studyType

        # 해당 study_type에 경험치 추가해주기
        studytype_list = db.session.query(Studytypelevel).filter_by(id=user_id).first()
        if study_type=="blog" :
            studytype_list.blog_lv = studytype_list.blog_lv + 1
        elif study_type=="main" :
            studytype_list.main_lv = studytype_list.main_lv + 1
        elif study_type=="argorithm" :
            studytype_list.argorithm_lv = studytype_list.argorithm_lv + 1
        elif study_type=="cs" :
            studytype_list.cs_lv = studytype_list.cs_lv + 1
        db.session.add(studytype_list)
        db.session.commit()

        # study_type 중에 제일 높은 숫자를 가진걸로 job 설정, 총 경험치, 레벨 구하기
        studytype_list = db.session.query(Studytypelevel).filter_by(id=user_id).first()
        data = {
            'blog_lv' : studytype_list.blog_lv,
            'algorithm_lv' : studytype_list.argorithm_lv,
            'main_lv' : studytype_list.main_lv,
            'cs' : studytype_list.cs_lv
        }
        job = max(data, key=data.get)
        total_exp = sum(data.values())
        level = get_level(required_exp, total_exp)

        # job, 경험치, 레벨 DB에 기록 (whale -> level, exp)
        whale_list = db.session.query(Whale).filter_by(id=user_id).first()
        whale_list.level = level
        whale_list.job = job
        whale_list.exp = total_exp
        db.session.add(whale_list)
        db.session.commit()





    # return {
    #     success : 
    # }

    # try :
    # except :