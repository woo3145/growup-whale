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
    time = datetime.now().strftime("%Y-%m-%D %H:%M:%S")
    return time

# 공부 시작
def studyStart(db) :
    print("studyStart")
    # if문 사용
    # id를 통해서 DB(user)에 시작시간(starttime)이 비워져 있는지 확인 (비워져 있다면 시작 시키고, 채워져 있다면 현재 진행중인 공부를 중단할지 물어보기)
    
    # 시작 시간을 DB에 기록하기 (user->starttime)

    # 어떤 버튼으로 공부 시작했는지 기록
    # study_type = 


# 공부 종료
def studyEnd(db) :
    print("studyEnd")
    # DB에서 시작시간 불러오기 (user->starttime), 종료시간 구해서 차이 (경험치) 만들기, 시작시간 삭제

    # 해당 study_type에 경험치 추가해주기

    # study_type 중에 제일 높은 숫자를 가진걸로 job 설정

    # 총 경험치와 레벨을 계산하여 DB에 기록 (whale -> level, exp)

    # level과 job에 맞는 이미지로 이미지 재설정





    # return {
    #     success : 
    # }

    # try :
    # except :