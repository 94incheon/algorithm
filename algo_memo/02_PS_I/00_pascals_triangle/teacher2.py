import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{} '.format(tc))
    N = int(input())
    
    tmp=[]
    result = [1]
    print(1)
    for i in range(N-1):
        result = [1]
        for j in range(i):
            result.append(tmp[j] + tmp[j+1])
        result.append(1)
        print(' '.join(map(str, result)))
        tmp = result
