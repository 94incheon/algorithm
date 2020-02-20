from pprint import pprint
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [ list(map(int, input().split())) for _ in range(N) ] # N x M 행렬 생성
    # pprint(matrix) 

    dx = [-1, 0, 1, 0] # 위 오른쪽 아래 왼쪽
    dy = [0, 1, 0, -1]

    s_list = []
    for x in range(N):
        for y in range(M):
            s = 0 + matrix[x][y]
            for i in range(1, matrix[x][y]+1):
                for j in range(4): # 위 오른 아래 왼 
                    nx = x + dx[j] * i # 새로운 x 좌표
                    ny = y + dy[j] * i # 새로운 y 좌표
                    if (0 <= nx <= N-1) and (0 <= ny <= N-1):
                        s += matrix[nx][ny]
            s_list.append(s)
    # print(s_list, ' --- S_list')

    print('#{} {}'.format(tc, max(s_list)))