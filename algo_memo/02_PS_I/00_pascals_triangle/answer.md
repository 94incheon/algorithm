```python
def pascal(a,b) :
    if a == b :
        return 1
    else :
        if b == 1 :
            return 1
        else :
            return pascal(a-1, b-1) + pascal(a-1, b)
T = int(input())
for t in range(1, 1+T) :
    N = int(input())
    print('#{}'.format(t))
    for i in range(1, 1+N) :
        for j in range(1,i+1) :
            print(pascal(i,j), end=' ')
        print()
```

