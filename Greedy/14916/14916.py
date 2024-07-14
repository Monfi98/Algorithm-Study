# 2원자리 동전과 5원짜리 동전은 무한정 많이 가지고있음
# 동전의 개수가 최소가 되도록 거슬러 주자.

# 거슬러 줄 수 없으면 -1을 출력하자

n = int(input())

# <13원 일경우>
# 5 + 5 + 3 안됨
# 5 + 8(2 + 2 + 2 + 2) -> 5
# solution: 5를 최대한 많이 넣고 하나씩 빼보면서 짝수인지 판별

# < 8원 일 경우>
# 5 + 안됨..
# 2 + 2 + 2 + 2

max_five_num = n // 5
result = 0

while True:
    remain_num = n - max_five_num * 5
    if remain_num % 2 == 0:
        result = max_five_num + remain_num // 2
        print(result)
        break
    max_five_num -= 1

    if max_five_num < 0:
        print(-1)
        break
    
