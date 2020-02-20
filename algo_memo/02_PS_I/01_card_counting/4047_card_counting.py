import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cards = input()
    # print(cards)
    # break
    hands = {'S':[], 'D':[], 'H':[], 'C':[]}
    for n in range(len(cards)//3):  # 12//3 = 4
        shape = cards[n*3]    # S
        number = cards[n*3+1:n*3+3]    # 01
        if number not in hands[shape]:
            hands[shape].append(number)
        else:
            print('#{} ERROR'.format(tc)) # 이미 겹치는 카드
            break
    # 포문 다 돌고나서 하는 행동
    else:
        result = [13-len(c) for c in hands.values()]
                                            # *언패킹 오퍼레이터
        print('#{} {} {} {} {}'.format(tc, *result))



    