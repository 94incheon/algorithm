import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    d = list(input())

    # counting 배열 생성 0~9 숫자
    c = [0] * 10

    for i in range(n):
        c[int(d[i])] += 1

    max_idx = 0
    max_value = c[0]
    # 위에서 초기화해줘서 1부터 시작
    for i in range(1, len(c)):
        if max_value <= c[i]:
            max_value = c[i]
            max_index = i

    print('#{} {} {}'.format(tc, max_index, max_value))

