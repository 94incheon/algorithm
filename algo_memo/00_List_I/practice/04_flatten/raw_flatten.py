import sys
sys.stdin = open('input.txt')

# sorting 방법으로 풀기

T = 10

for tc in range(1, T+1):
    n = int(input()) # 덤핑 횟수
    d = list(map(int, input().split())) # 데이터

    # 덤핑 과정 반복
    for c in range(n):
        max_idx = 0
        min_idx = 0

        # 가장 값이 큰 친구의 인덱스를 찾는과정
        for i in range(1, 100):
            # 최고 idx 찾기
            if d[max_idx] < d[i] :
                max_idx = i
            # 최저 idx 찾기
            if d[min_idx] > d[i] :
                min_idx = i
        
        d[max_idx] -= 1
        d[min_idx] += 1

    # 덤핑이 끝난 시점 => 최대값 - 최소값
    max_value = d[0]
    min_value = d[0]

    for j in range(1, 100):
        if max_value < d[j] :
            max_value = d[j]

        if min_value > d[j] :
            min_value = d[j]


    print('#{} {}'.format(tc, max_value - min_value))