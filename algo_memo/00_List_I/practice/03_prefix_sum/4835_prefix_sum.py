# 부분합(구간합) 문제, 중요(빈번)

import sys
sys.stdin = open('input.txt')



T = int(input())

for tc in range(1, T+1):
    # 갯수, 구간수
    N, M = map(int, input().split())
    d = list(map(int, input().split()))
    
    # 구간합들이 모여있는 arr 생성
    arr = []
    # N-M+1 번 돈다... 중요
    for i in range(N-M+1):
        # 인덱스 + 구간만큼 
        arr.append(sum(d[i:i+M]))

    print('#{} {}'.format(tc, max(arr) - min(arr)))