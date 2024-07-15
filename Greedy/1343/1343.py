# AAAA와 BB 가 있음
# .와 X 로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'
# X를 모두 폴리오미노로 덮어야하고, .는 덮으면안됨


# < XXXXXX > -> 6
# < XX.XX > -> 2, 2
# < XX.XXXXXXXXXX..XXXXXXXX...XXXXXX >
# -> 2, 6, 0, 8, 0, 0, 6

board = input()
board += '.'
result = ''
count = 0

for i in range(len(board)):
    if board[i] == 'X':
        count += 1
    elif board[i] == '.':
        # count = 3
        max_num = count // 4 # 0, 1, 2
        for j in range(max_num + 1, 0, -1):
            # 2부터
            if (count - j * 4) % 2 == 0:
                result += 'AAAA' * max_num + 'BB' * ((count - max_num * 4) // 2) + '.'
                break

        count = 0

if len(result) == len(board):
    print(result[0:-1])
else:
    print(-1)