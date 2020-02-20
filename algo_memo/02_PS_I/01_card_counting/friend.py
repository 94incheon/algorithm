T = int(input())
for tc in range(1, T+1):
    trumps = {
        'S':[0 for _ in range(1, 14)],
        'D':[0 for _ in range(1, 14)],
        'H':[0 for _ in range(1, 14)],
        'C':[0 for _ in range(1, 14)],
    }
    pattern = [val for val in trumps.keys()]
    cards = input()
    tmp = [(card, cards[idx+1:idx+3]) for idx, card in enumerate(cards) if card in pattern]
    flag = 1
    for pat, num in tmp:
        trumps[pat][int(num)-1] += 1
        if trumps[pat][int(num)-1] > 1:
            flag = 0
    if flag == 0:
        result = "ERROR"
    else:
        result = []
        for key, val in trumps.items():
            result.append(val.count(0))
        result = ' '.join(map(str, result))
    print('#{} {}'.format(tc, result))