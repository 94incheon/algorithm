import sys
sys.stdin = open('input.txt')

T=10
for tc in range(1, T+1):
    dump = int(input()) # 덤프 횟수
    d = list(map(int, input().split()))

    for _ in range(dump):
        d.sort() # 덤프할때마다 다시 정렬해야하므로..
        d[-1] -= 1
        d[0] += 1


    res = max(d)-min(d)
    print('#{} {}'.format(tc, res))
