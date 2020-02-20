n = 1357

# 단조증가 하는지 체크하는 함수 check()
def check(n):
    n, r = n // 10, n % 10 # n : 몫, r : 나머지

    while n != 0:
        if n%10 > r:
            return False
        n, r = n//10, n%10

    return True

print(check(n))