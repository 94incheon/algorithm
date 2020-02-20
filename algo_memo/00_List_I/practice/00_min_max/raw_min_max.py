import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    d = list(map(int, input().split()))

    # max_num = max(d)
    # min_num = min(d)
    
    max_num = d[0]
    min_num = d[0]

    for i in range(1, n):
        if max_num < d[i]:
            max_num = d[i]
        if min_num > d[i]:
            min_num = d[i]

    print('#{} {}'.format(tc, max_num - min_num))
