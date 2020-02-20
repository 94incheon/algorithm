# Ai * Aj
# [x,y,z]
# 단조증가 하는지...
# max[y, z, a]
import sys
sys.stdin = open('input.txt')

def check(n):
    n, r = n // 10, n % 10 # n : 몫, r : 나머지

    while n != 0:
        if n%10 > r:
            return False
        n, r = n//10, n%10

    return True

# =================================================

T=int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = -1


    for i in range(N):
        for j in range(i+1, N):
            num = numbers[i] * numbers[j]
            if result < num:
                if check(N):
                    result = num

    print('#{} {}'.format(tc, result))

