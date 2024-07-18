# 2+1 행사

# 가장 싼 것은 무료로 지불하고 나머지 두 개의 제품 가격만 지불하면 된다.
# 한 번에 3개의 유제품을 사지 않는다면 할인 없이 정가를 지불해야 한다.
# 정답은 2^31 - 1보다 작거나 같다.

# 10, 9, 4, 2, 6, 4, 3
# (10, 9, 6) (4, 4, 3) (2)
# 15, 7, 2

# 3, 2, 3, 2
# (3, 2, 2) (3) -> 8
# (3, 3, 2) (2) -> 8


# 가장 싼것은 무료로 지불 -> 
n = int(input())
cost_list = []
for i in range(n):
    cost = int(input())
    cost_list.append(cost)

cost_list.sort(reverse=True)
result = 0
# print(cost_list)
for i in range(n):
    if (i + 1) % 3 != 0:
        # print('add',cost_list[i])
        result += cost_list[i]

print(result)