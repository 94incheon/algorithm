from pprint import pprint
import sys
sys.stdin = open('input.txt')

def red(matrix, r1, c1, r2, c2):
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
            elif matrix[i][j] == 2:
                matrix[i][j] = 3
    return matrix

def blue(matrix, r1, c1, r2, c2):
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if matrix[i][j] == 0:
                matrix[i][j] = 2
            elif matrix[i][j] == 1:
                matrix[i][j] = 3
    return matrix



T = int(input())

for tc in range(1, T+1):
    res = 0
    # 10x10 2차원배열 생성
    matrix = [[0] * 10 for _ in range(10)]
    # pprint(matrix)

    # 칠할 영역 개수
    N = int(input())
    for _ in range(N):
        d = list(map(int, input().split()))
        c = d[4]
        # 빨간
        if c == 1:
            matrix = red(matrix, d[0], d[1], d[2], d[3])
        # 파랑
        else:
            matrix = blue(matrix, d[0], d[1], d[2], d[3])

    cnt = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                cnt += 1
    res = cnt
    print('#{} {}'.format(tc, res))




