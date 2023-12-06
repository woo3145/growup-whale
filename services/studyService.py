import math
from datetime import datetime

TOTAL_EXP = 71280
MAX_LEVEL = 5

# 각 레벨의 경험치 (exp_for_level) 계산
C = TOTAL_EXP / sum(math.log(level) for level in range(1, MAX_LEVEL +1))
exp_for_level = [int(C*math.log(level)) for level in range(1, MAX_LEVEL +1)]
print("각 레벨의 경험치 : ", exp_for_level)

# 시작, 종료 시간 구하기 
def get_time() :
    time_str = get_time()
    time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    return time

# 경험치 (공부시간) 구하기...
def get_exp(start_time, end_time) :
    study_time = end_time - start_time
    return study_time.seconds // 60

# level 구하기
def get_level(total_exp) :
    level = 0
    if total_exp < exp_for_level[1] : 'Lv.0'
    elif total_exp < exp_for_level[2] : 'Lv.1'
    elif total_exp < exp_for_level[3] : 'Lv.2'
    elif total_exp < exp_for_level[4] : 'Lv.3'
    elif total_exp >= exp_for_level[4] : "성장 완료!"
    return level


# 공부 시작
def studyStart(db) :
    print("studyStart")
    
    # id 이용해서 DB(user)에 시작시간(starttime)이 비워져 있는지 확인 (if문 : 비워져 있다면 공부 시작 시키고, 채워져 있다면 현재 진행중인 공부를 중단할지 물어보기) 
    user_list = db.user.query.filter_by(id=1).first()
    print(user_list)
    if user_list[0].starttime is not None :   
        print("시작 시간이 채워져있습니다. 해당 공부를 종료하고, 다른 공부를 진행?")
        studyEnd()

    else : 
        print("시작 시간이 비어있습니다!")

        # 시작 시간을 DB에 기록하기 (user->starttime)
        time = get_time()
        print(f"시작시간 {time}")
        
        # 어떤 버튼으로 공부 시작했는지 기록
        # study_type = 


# 공부 종료
def studyEnd(db) :
    print("studyEnd")

    # DB에서 시작시간 불러오기 (user->starttime)
    user_list = db.user.filter_by(id=1).first()
    start_time = user_list[0].starttime

    # 시작 시간 삭제
    user_list.starttime = None
    db.session.add(user_list)
    db.session.commit()

    # 종료시간 구해서 차이 (경험치) 만들기
    end_time = get_time()
    exp = get_exp(start_time, end_time)
    print(exp)

    # 해당 study_type에 경험치 추가해주기
    studytype_list = db.studytypelevel.filter_by(id=1).first()
    db.studytypelevel.blog_lv = exp
    db.sesseion.add(studytype_list)

    # study_type 중에 제일 높은 숫자를 가진걸로 job 설정
    data = {
        'blog_lv' : studytype_list[0].blog_lv,
        'algorithm_lv' : studytype_list[0].algorithm_lv,
        'main_lv' : studytype_list[0].main_lv,
        'cs' : studytype_list[0].cs_lv
    }
    job = max(data, key=data.get)

    # 총 경험치와 레벨을 계산하여 DB에 기록 (whale -> level, exp)
    total_exp = sum(data.values())
    print(total_exp)
    whale_list = db.whale.filter_by(id=1).first()
    whale_list.level = get_level(exp)
    whale_list.job = job
    whale_list.exp = exp
    db.session.add(whale_list)
    db.session.commit()



    # return {
    #     success : 
    # }

    # try :
    # except :