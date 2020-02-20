import sys
# from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # matrix = [[0 for _ in range(N)] for _ in range(N)]
    matrix = [[0]*N for _ in range(N)]
    # pprint(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i==j:
                matrix[i][j] = 1
            elif j>i:
                matrix[i][j] = 0
            elif j == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]

    # pprint(matrix)
    # 출력
    print('#{}'.format(tc))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i >= j:
                print(matrix[i][j], end =' ')
        print()

