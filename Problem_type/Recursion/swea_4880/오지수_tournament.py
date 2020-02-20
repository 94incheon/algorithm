# 토너먼트 카드게임
winner = [[1, 2], [3, 1], [2, 3]]

def game(match):
    if len(match) == 2:
        temp = [match[0][1], match[1][1]]
        if temp in winner:
            return match[1]
        elif temp[::-1] in winner:
            return match[0]
        elif temp[0] == temp[1]:
            if match[0][0] < match[1][0]:
                return match[0]
            else:
                return match[1]
    elif len(match) == 1:
        return match[0]
    else:
        match1 = match[:(1+len(match))//2]
        match2 = match[(1+len(match))//2:]
        return game([game(match1), game(match2)])
        

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    match = list(map(int, input().split()))
    result = game(list(enumerate(match)))
    print('#{} {}'.format(tc, result[0]+1))