# PT를 한 번 받을 때 운동기구를 최대 두 개까지만 선택할 수 있다.

# PT를 받을때마다 이전에 사용하지 않았던 운동기구를 선택하기로 계획을 세웠다.
# 비용을 절약하기 위해 PT를 받을 때 운동기구를 되도록이면 두 개를 사용하기로 했다.

# 10개 운동기구 -> PT 5번
# 9개 운동기구 -> PT 5번

# 어떤 운동기구는 근손실이 적게 일어나는데 어떤 운동기구는 자극이 잘 와서 근손실이 많이 일어난다.
# 근손실 정도가 M을 넘지 않도록 하고 싶다.
# 이때, M의 최솟값을 구해보자.

# 5 -> PT 3번
# 1 2 3 4 5 
# 15, 23, 34

# 4 8 10 20 21
# 24 18 21 M = 24


n = int(input())

machine_list = list(map(int, input().split(" ")))
machine_list.sort()

last_num = 0

if n % 2 == 1: # 홀수라면
    n -= 1
    machine_list.pop()

# 8 // 4
max_num = 0

for i in range(n // 2):
    current_num = machine_list[i] + machine_list[n - i - 1]
    print(current_num)
    if max_num < current_num:
        max_num = current_num

print(current_num)

