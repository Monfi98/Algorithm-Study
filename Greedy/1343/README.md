# 1343번 폴리오미노

## 문제
민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB

이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, '.'는 폴리오미노로 덮으면 안 된다.

폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.

## 입력
첫째 줄에 보드판이 주어진다. 보드판의 크기는 최대 50이다.

## 출력
첫째 줄에 사전순으로 가장 앞서는 답을 출력한다. 만약 덮을 수 없으면 -1을 출력한다.


## 내 정답
```Python
board = input()
board += '.'
result = ''
count = 0

for i in range(len(board)):
    if board[i] == 'X':
        count += 1
    elif board[i] == '.':
        max_num = count // 4
        for j in range(max_num + 1, 0, -1):
            if (count - j * 4) % 2 == 0:
                result += 'AAAA' * max_num + 'BB' * ((count - max_num * 4) // 2) + '.'
                break

        count = 0

if len(result) == len(board):
    print(result[0:-1])
else:
    print(-1)
```