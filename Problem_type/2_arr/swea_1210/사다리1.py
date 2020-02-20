import sys
sys.stdin = open('input.txt')
#==========================================================================================
#                            위에서 아래로 내려가는 코드
#==========================================================================================

T = 10
for tc in range(1, T+1):
    N = int(input())
    d = [list(map(int, input().split())) for _ in range(100)] # 100 x 100 사다리 2차원 배열
    for idx, val in enumerate(d[0]):
        if val == 1:
            res = idx
            x, y = 0, idx # 행렬 맨 첫줄에 있는 1 들의 좌표 # (0, 67)
            n=0
            while x != 100:
                if y!=0 and d[x][y-1]: # 왼쪽값 검사
                    while y>0 and d[x][y-1]:
                        y -= 1

                elif y!=99 and d[x][y+1]:
                    while y<99 and d[x][y+1]:
                        y += 1

                x += 1
                if 0<=x<=99 and 0<=y<=99:
                    n = d[x][y]

            if n == 2:
                print('#{} {}'.format(tc, res))


#==========================================================================================
#                            아래에서 위로 올라오는 코드
#==========================================================================================
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     d = [ list(map(int, input().split())) for _ in range(100) ]

#     for idx, val in enumerate(d[-1]):
#         if val == 2:
#             y = idx

#     result = 0
#     x = 99
#     # print(x,y, '2의 좌표') # 2 의 좌표


#     while x!=0: # x가 0 이 될때까지
#         if y!=99 and d[x][y+1]:
#             while y<99 and d[x][y+1]:
#                 y += 1

#         elif y!=0 and d[x][y-1]:
#             while y>0 and d[x][y-1]:
#                 y -= 1
#         x -= 1

#     # print(x,y, '사다리 다 올라간뒤 변한 좌표')
#     print('#{} {}'.format(tc, y))

            