import math
from datetime import datetime

total_exp = 71280
max_level = 5

# 각 레벨의 경험치 (exp_for_level) 계산
C = total_exp / sum(math.log(level) for level in range(1, max_level +1))
exp_for_level = [int(C*math.log(level)) for level in range(1, max_level +1)]
print("각 레벨의 경험치 : ", exp_for_level)

# 시간 구하기 (시작, 종료)
def get_time() :
    time_str = get_time()
    time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    return time


# 시작 시간
start_time_str = get_time()
start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
print(start_time)

# 종료 시간
end_time_str = '2023-12-06 22:47:11'
end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")

# 공부한 시간 & 분단위 표현
study_time = end_time - start_time
minute = study_time.seconds // 60




# 공부 시작
def studyStart(db) :
    print("studyStart")
    
    # id 이용해서 DB(user)에 시작시간(starttime)이 비워져 있는지 확인 (if문 : 비워져 있다면 공부 시작 시키고, 채워져 있다면 현재 진행중인 공부를 중단할지 물어보기) 
    user_list = db.user.query.filter_by(id='값').first()
    if user_list[0].starttime is None :
        print("시작 시간이 비어있습니다!")

        # 시작 시간을 DB에 기록하기 (user->starttime)
        time = get_time()
        print(f"시작시간 {time}")
        
        # 어떤 버튼으로 공부 시작했는지 기록
        # study_type = 
    else : 
        print("시작 시간이 채워져있습니다. 해당 공부를 종료하고, 다른 공부를 진행?")
        # 
    



# 공부 종료
def studyEnd(db) :
    print("studyEnd")

    # DB에서 시작시간 불러오기 (user->starttime), , 시작시간 삭제
    user_list = db.user.query.filter_by(id='값').first()
    start_time = user_list[0].starttime

    # 종료시간 구해서 차이 (경험치) 만들기
    time = get_time()
    print(f"종료시간 {time}")
    study_time = end_time - start_time
    exp = study_time.seconds // 60

    # 해당 study_type에 경험치 추가해주기

    # study_type 중에 제일 높은 숫자를 가진걸로 job 설정

    

    # 총 경험치와 레벨을 계산하여 DB에 기록 (whale -> level, exp)

    # level과 job에 맞는 이미지로 이미지 재설정





    # return {
    #     success : 
    # }

    # try :
    # except :