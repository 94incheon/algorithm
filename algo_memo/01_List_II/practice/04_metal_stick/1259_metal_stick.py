import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 나사의 수
    N = int(input())
    d = list(map(int, input().split()))
    # print(d)

    # pipes = [ [d[i], d[i+1]] for i in range(0, N*2, 2) ]
    pipes = []
    for i in range(0, N*2, 2):
        pipes.append([d[i], d[i+1]])

    # print(pipes)

    # 파이프들중에 하나를 뽑을 것
    connected = pipes.pop()
    
    # pipes 가 빌때까지.
    while pipes:
        for i in range(len(pipes)):
            if pipes[i][0] == connected[-1]:
                connected += pipes.pop(i)
                break
            if pipes[i][-1] == connected[0]:
                connected = pipes.pop(i) + connected
                break


    # print(connected)
    
    print('#{} {}'.format(tc, ' '.join(map(str, connected))))
