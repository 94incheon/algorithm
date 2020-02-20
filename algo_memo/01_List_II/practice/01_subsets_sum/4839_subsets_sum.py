# 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합
import sys
sys.stdin = open('input.txt')
from itertools import combinations
from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 12까지의 원소 중 N개가 포함된 부분집합
    subsets = combinations(range(1, 13), N)

    # cnt = 0
    # for subset in subsets:
    #     if sum(subset) == K:
    #         cnt += 1

    cnt = sum( [1 for subset in subsets if sum(subset) == K ] )

    print('#{} {}'.format(tc, cnt))
