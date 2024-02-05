#   date : 2024-02-01
#   file : test25_wed.py
#   desc : urllib 모듈 사용법

# from urllib.request import  # request 모듈안의 모든 내용 다 사용할 때
# from urllib.request import Request, urlopen  # Request 클래스와 urllib만 쓰겠다

# req = Request('https://www.naver.com/') # 네이버 웹주소(url)
# res = urlopen(req) #url주소로 웹사이트 열어달라고 요청

# print(f'응답 코드는 : {res.status}') #url로 요청된 웹사이트 응답 확인
# print(res.read())

# #urllib.request보다 성능이 조금 더 나은 모듈
# import requests

# res2 = requests.get('https://www.naver.com/')
# print(res2.status_code)
# print(res2.text)

# import random

# def getRandomNumber():
#     number = random.randint(1, 45)
#     return number # 1. 함수를 맹글어 줘요

# lotto = []
# count = 0

# while True: # 중복이 없는 6개의 숫자가 나올 때 까지 계속 반복해라
#     if count > 5:
#         break # 6개의 중복 없는 숫자가 나오면 탈출 시켜줄게
#     random_number = getRandomNumber()
#     if random_number not in lotto: # 뽑은 랜덤숫자가 중복아니면
#         lotto.append(random_number) # 리스트에 좀 껴줘라
#         count += 1 # 탈출 시켜줘야하니까 다 충족했음 count하나 높여줘라

# print(lotto)


import random

lotto=[]
n=0

while len(lotto) < 6:
    num=random.randint(1,45)   # 1~45까지의 난수
    if(lotto.count(num)==0):   # 이미 생성된 번호가 아니면 (중복 수 체크)
        lotto.append(num)
lotto.sort()   # 크기 순 정렬
print(lotto)