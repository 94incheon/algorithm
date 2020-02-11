import sys
sys.stdin = open('input.txt')

T=10
for tc in range(1,T+1):
    N = int(input())
    d = list(map(int, input().split()))

    temp = []
    for i in range(2, N-2): # i = 2
        s = 0
        a1 = d[i-2:i] + d[i+1:i+3]
        if d[i] - max(a1) > 0:
            s += d[i] - max(a1)
        else:
            s += 0
        temp.append(s)

    print('#{} {}'.format(tc, sum(temp)))