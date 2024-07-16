# 로프를 사용하여 물체를 들어올릴 수 있음
# 여러개의 로프를 병렬로 연결하면 로프에 걸리는 중량을 나눌 수 있음
# 이 로프들을 이용해 들어올릴 수 있는 물체의 최대 중량을 구하라.

# 2
# 10 -> 10
# 15 -> 10
# 답: 20

n = int(input())

rope_list = []
for i in range(n):
    rope = int(input())
    rope_list.append(rope)

rope_list.sort()
result = 0

for i in range(n):
    num = rope_list[i] * (n - i)
    if result < num:
        result = num


print(result)
