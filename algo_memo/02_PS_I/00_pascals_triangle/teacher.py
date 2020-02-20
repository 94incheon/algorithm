import sys
sys.stdin = open('input.txt')

def pascal(x, y):
    if y == 0 or x == y:
        return 1
    elif y < 0 or x < y:
        return 0
    return pascal(x-1, y-1) + pascal(x-1, y)


# 재귀버전
T = int(input())
for tc in range(1, T+1):
    print('#{} '.format(tc))
    N = int(input())

    for i in range(N):
        for j in range(i+1):
            print(pascal(i,j), end=' ')
        print()











# 재귀 
# 1. base case : 
#    - 정답을 찾았을 때, 
#    - 못 찾았을 때,

# 2. recursive step : 
#    - 계속 가야할 때

# 3. 데이터(누적) : 인자