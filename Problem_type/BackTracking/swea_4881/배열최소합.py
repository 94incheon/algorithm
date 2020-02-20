import sys
sys.stdin = open('input.txt')

def solution(size, s, sums):
    if size == s:
        result.append(sums)
        return
    if sums > min(result): # 백트래킹..
        return

    else:
        for i in range(size):
            if visited[i] == False:
                visited[i] = True
                n_sum = matrix[s][i]
                solution(size, s+1, sums+n_sum)
                visited[i] = False


T=int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    #print(matrix)

    result = [10000]
    solution(len(matrix), 0, 0)
    # print(result)
    print('#{} {}'.format(tc, min(result)))