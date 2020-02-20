from pprint import pprint
import sys
sys.stdin = open('input.txt')

T = 1
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(5)]
    res = 0
    pprint(matrix)

    # 출발하는 1의 x 좌표를 r_list 에 넣기
    r_list = []
    s_list = [] # 이동거리 모으기
    for idx, start in enumerate(matrix[0]):
        if start == 1:
            r_list.append(idx)
            # 이동거리 s
            s = 1



    # 











    

    # print('#{} {}'.format(tc, res))
