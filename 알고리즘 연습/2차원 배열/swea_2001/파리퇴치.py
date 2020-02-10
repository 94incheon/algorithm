from pprint import pprint
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    pprint(matrix)

    max_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1): # 0, 1, 2, 3
            kill = 0
            for k in range(M): # k : 0, 1
                kill += sum(matrix[i+k][j:j+M])
            if kill > max_kill:
                max_kill = kill

    res = max_kill
    print('#{} {}'.format(tc, res))