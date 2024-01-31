#   date : 2024-01-31
#   file : test19_starprint.py
#   desc : 별찍기 또는 피라미드 만들기
# *
# **
# ***
# ****
# *****
#
for i in range(1, 5+1):
    # i가 1이면, range(1,2) 1번반복
    # i가 2이면, range(1,3) 두번 반복
    for j in range(1, 5-i+1): 
        print('*', end='') # 엔터 대신 empty로 변환
    print() # 안쪽 for문이 끝나면 엔터