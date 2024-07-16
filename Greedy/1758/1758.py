# 8시가 될 때 까지 문앞에 줄세워 놓는다.
# 손님들은 자기가 커피를 몇 번째 받는지에 따라 팁을 다른 액수로 강호에게 준다.

# 돈 - (받은 등수 - 1) 만큼 팁을 줌
# 음수라면 돈 받을 수 없음

# 강호가 받을 수 있는 팁의 최대값을 출력

n = int(input())

tip_list = []
for i in range(n):
    money = int(input())
    tip_list.append(money)

tip_list.sort(reverse=True)

result = 0
for i in range(n):
    if tip_list[i] - i < 0:
        break
    else:
        result += tip_list[i] - i

print(result)


# 5
# 7
# 8
# 6
# 9
# 10

# 30

# 10 - (1 - 1) = 10
# 9 - (2 - 1) = 8
# 8 - (3 - 1) = 6
# 7 - (4 - 1) = 4
# 6 - (5 - 1) = 2

