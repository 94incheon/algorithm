# 백트래킹

> swea_4881_배열최소합
>
> [참고 블로그](https://m.blog.naver.com/ydot/221387998142)



- 파이썬에서 제공하는 최대값 상수를 이용

  - ```python
    import 
    max = sys.maxsize
    min = -sys.maxsize-1
    ```



- 백트래킹 기반의 재귀 함수를 이용한다.

  - ```python
    def f(row, score):
        for i in range(3):
            f(row+1, score+matrix[row][i])
    ```

  

- 한 번 선택한 항목을 다시 선택하지 않도록 하기위해 별도의 플래그 배열을 사용한다.

  - ```python
    checked = [False, False, False]
    ```



```python
def f(row, score):
    for i in range(3):
        if checked[i] == False:
            checked[i] = True
            f(row+1, score+matrix[row][i])
            # 재귀 호출에서 빠져나오면 현재 선택한 항목을 해제하여 선택하지않은것으로 다음에 처리
            checked[i] = False
```



```python
False = 0
True = 1
INT_MAX = 10000

matrix = [
    [1, 5, 3],
    [2, 5, 7],
    [5, 3, 5]
]

col_check = [ False, False, False ]
min_sol = INT_MAX

def f(row, score):
    global min_sol
    
    if row == 3:
        if score < min_sol:
            min_sol = score
        return min_sol
    
    for i in range(3):
        if col_check[i] = False:
            col_check[i] = True
            f(row+1, score+matrix[row][i])
            col_check[i] = False
            
    return min_sol

if __name__ == '__main__':
    print("min_sol : %d" % f(0,0))
```

