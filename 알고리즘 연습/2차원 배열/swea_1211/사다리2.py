import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    d = [ list(map(int, input().split())) for _ in range(100) ]

    # 가장 짧은 이동거리 시작지점 x 좌표 출력
    
    temp = [] # 좌표랑 이동거리 같이 담는 list
    cnt_list = [] # 이동거리들 담는 list
    idx_list = [] # Y좌표 -> 문제에서는 이걸 x좌표라고 표시해놨음

    for idx, val in enumerate(d[0]):
        if val == 1:
            y = idx
            x = 0
            # print(x, y) 첫번째 행의 1 들의 좌표
            cnt=0
            while x<=99:
                
                if y>0 and d[x][y-1]: # 왼쪽값이 있을때
                    while y>0 and d[x][y-1]:
                        y -= 1
                        cnt += 1
                elif y<99 and d[x][y+1]: # 오른쪽 값이 있을때
                    while y<99 and d[x][y+1]:
                        y += 1
                        cnt += 1
                x += 1
                cnt += 1
            idx_list.append(idx)
            cnt_list.append(cnt)
            temp.append([idx, cnt])

    # print(temp)
    # print(min(cnt_list))
    res = []
    for aa in temp:
        if aa[1] == min(cnt_list):
            res.append(aa[0])
    # print(res)

    print('#{}'.format(tc), end=' ')
    for r in res:
        print(r)