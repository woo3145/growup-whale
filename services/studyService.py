from flask import Flask
from datetime import datetime





# # 공부 타입 받아오기
# def confirmButton(endpoint, text, icon) :
#     result = {endpoint, text}
#     return result



# 공부 종료
def studyEnd(db, required_exp) :
    print("studyEnd")

    # 해당 study_type에 경험치 추가해주기
    studytype_list = db.studytypelevel.filter_by(id=1).first()
    db.studytypelevel.blog_lv = exp
    db.sesseion.add(studytype_list)

    # # study_type 중에 제일 높은 숫자를 가진걸로 job 설정
    # data = {
    #     'blog_lv' : studytype_list[0].blog_lv,
    #     'algorithm_lv' : studytype_list[0].algorithm_lv,
    #     'main_lv' : studytype_list[0].main_lv,
    #     'cs' : studytype_list[0].cs_lv
    # }
    # job = max(data, key=data.get)

    # # 총 경험치와 레벨을 계산하여 DB에 기록 (whale -> level, exp)
    # total_exp = sum(data.values())
    # print(total_exp)
    # whale_list = db.whale.filter_by(id=1).first()
    # whale_list.level = get_level(exp)
    # whale_list.job = job
    # whale_list.exp = exp
    # db.session.add(whale_list)
    # db.session.commit()



    # return {
    #     success : 
    # }

    # try :
    # except :