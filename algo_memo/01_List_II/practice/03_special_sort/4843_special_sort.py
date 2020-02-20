import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 받아온 데이터 정렬
    d = sorted(list(map(int, input().split())))
    r = d[-5:][::-1]
    print('#{}'.format(tc), end=' ')
    for i, j in zip(r, d[:5]):
        print(i, end=' ')
        print(j, end=' ')
    print()

