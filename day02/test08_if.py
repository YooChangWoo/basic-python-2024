#   date : 2024-01-30
#   desc : 홀수/짝수 구분

number = int(input('정수입력 >')) # 입력 받은 후 정수로 변경

if number % 5 == 0: # 짝수 또는 배수
    print('5의 배수!')
else: # 홀수 , 작성을 하던 중 끊어야 하는 상황이 생길 때 pass 하면됨
    print('나머지수!')

