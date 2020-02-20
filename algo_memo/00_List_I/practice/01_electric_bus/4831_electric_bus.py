import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    d = list(map(int, input().split()))

    # 출발선 지어주기
    d.insert(0, 0)
    # 마지막 정류장
    d.append(N)

    # 마지막 충전기 위치
    last = 0
    # 몇번 충전했는지 카운팅
    cnt = 0

    # 
    for i in range(1, M+2):
        if d[i] - d[i-1] > K:
            cnt = 0
            break
        if d[i] > last + K:
            last = d[i-1]
            cnt += 1

    print('#{} {}'.format(tc, cnt))

