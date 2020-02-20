import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(N)]

    # 파리채가 순회하는 횟수
    kill = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0 # 파리 총합
            for k in range(M):
                s += sum(d[i+k][j:j+M])    # 이 부분 이해하는것이 가장 중요
            kill.append(s)
    
    print('#{} {}'.format(tc, max(kill)))