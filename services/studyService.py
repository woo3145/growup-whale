import math

total_exp = 71280
max_level = 5

# 상수 C 계산
C = total_exp / sum(math.log(level) for level in range(1, max_level +1))
                    
# 각 레벨의 경험치 계산
exp_for_level = [int(C*math.log(level)) for level in range(1, max_level +1)]

print("각 레벨의 경험치 : ", exp_for_level)

# def studyStart() :
#     print("studyStart")
    # return {
    #     success : 
    # }


# def studyEnd() :
#     print("studyEnd")