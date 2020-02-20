import sys
sys.stdin = open('input.txt')

# 구간합
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    d = list(map(int, input().split()))

    # min, max 트래킹, // 임의의 min 밸류는 크게 잡아줘야..
    max_value = 0
    min_value = 1000000

    for i in range(N-M+1):
        s = 0
        for j in range(i, i+M):
            s += d[j]
        if s > max_value:
            max_value = s
        if s < min_value:
            min_value = s
    
    print('#{} {}'.format(tc, max_value - min_value))
