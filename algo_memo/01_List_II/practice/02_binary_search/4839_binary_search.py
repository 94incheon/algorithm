import sys
sys.stdin = open('input.txt')

T = int(input())

def find(total, target):
    # 쪽수로 할 지, 인덱스를 기준으로 할지.. 여기서는 쪽 수를 기준으로 한다.
    l = 1
    r = total # 쪽수 400
    m = int((l+r)/2)  # //(몫) 오퍼레이터를 써도되고 int() 를써도된다. int 도 소수점을 버려서 // 가 비슷
    cnt = 1

    # 몇번 돌려야 할지 모를때 for문보다 while문이 적합하다.
    # 1~9 까지 숫자 중 target이 3 일 경우,

    while m != target: # 중간값이 target 과 같지 않으면 계속 실행
        # m : 5
        # target : 7
        if m < target:
            l = m
        # m : 5
        # target : 3
        else:
            r = m
        m = int((l+r)/2)
        cnt += 1

    return cnt


for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    A = find(P, Pa)
    B = find(P, Pb)

    result = '0'
    if A < B :
        result = 'A'
    elif A > B:
        result = 'B'

    print('#{} {}'.format(tc, result))
    
