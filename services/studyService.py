
# 레벨 구하기
def get_level(required_exp, total_exp) :
    level = 0
    if total_exp >= 99 : level = 5
    elif total_exp >= required_exp['4'] and total_exp < 99 : level = 4
    elif total_exp >= required_exp['3'] and total_exp < required_exp['4'] : level = 3
    elif total_exp >= required_exp['2'] and total_exp < required_exp['3'] : level = 2
    elif total_exp < required_exp['2'] : level = 1
    return level



def studyCheck(db, User, Whale, Studytypelevel, required_exp, studyType) :
    print(required_exp)
    # 유저 이메일 받아오기
    # email = 

    # 클릭한 버튼 찾아내기 (O)
    study_type = studyType

    # 해당 study_type에 경험치 추가해주기 (O ? work_out(운동하기) 버튼의 경우는 어떻게 처리)
    studytype_list = db.session.query(Studytypelevel).filter_by(id=1).first()
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
    studytype_list = db.session.query(Studytypelevel).filter_by(id=1).first()
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
    whale_list = db.session.query(Whale).filter_by(id=1).first()
    whale_list.level = level
    whale_list.job = job
    whale_list.exp = total_exp
    db.session.add(whale_list)
    db.session.commit()

    # level -> job -> 0 (whale name, url)




    # return {
    #     success : 
    # }

    # try :
    # except :