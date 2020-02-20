# 1208_flatten.py
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    n = int(input()) # 덤프 횟수
    d = list(map(int, input().split())) # 상자높이들 data (d)

    # 덤프 횟수만큼 돈다.
    for c in range(n):

        # 1. 가장 높은 박스에서 -1
        # 2. 가장 낮은 박스에서 +1
        d.sort()
        d[0] += 1 # 최소값
        d[-1] -= 1 # 최대값

    # 최대에서 최소를 빼주면 됨. 최대-최소 높이차 출력.
    print('#{} {}'.format(tc, max(d)-min(d)))


