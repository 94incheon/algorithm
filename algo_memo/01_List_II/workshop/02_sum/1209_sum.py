import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    c = 100
    n = int(input())
    # 2차원 배열 생성 100x100행렬
    d = [list(map(int, input().split())) for _ in range(c)]

    m = 0

    # 행 우선 순회
    for i in range(c):
        s = 0
        for j in range(c):
            s += d[i][j]
        if s > m:
            m = s

    # print(i, j)
    # i, j 를 또 쓰는것은 위에서 반복문이 다 끝났기 때문에 사용가능    

    # 열 우선 순회
    for i in range(c):
        s = 0
        for j in range(c):
            s += d[j][i]
        if s > m:
            m = s

    # 대각선 합 구하기 (\)
    s = 0
    for i in range(c):
        s += d[i][i]
    if s > m:
        m = s

    # 대각선 합 구하기 (/)
    s = 0
    for i in range(c):
        # s += d[i][c-1-i]
        s += d[i][-(i+1)]
    if s > m:
        m = s
    
    print('#{} {}'.format(tc, m))
