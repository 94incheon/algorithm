def min_sum(n, k, temp):
    global s
    if temp > s:
        return
    if n == k:
        if temp < s:
            s = temp
            return
    else:
        for i in range(k):
            if used[i] == 0:
                used[i] =1
                result[n] = i
                value = data[n][i]
                min_sum(n+1, k, temp + value)
                used[i] = 0

T = int(input())

for t in range(1, T+1):
    N = int(input())
    data = [ list(map(int, input().split())) for _ in range(N)]
    

    length = len(data)
    result = [0] * length
    used = [0] * length
    s = 100000
    min_sum(0, length, 0)

    print('#{} {}'.format(t,s))