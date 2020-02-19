dx = [0, 1, 0, -1] # 우 하 좌 상
dy = [1, 0, -1, 0]

def find_start(arr):
    res = 0, 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == '2' :
                return i, j
                break

def DFS(arr, x, y):
    s = []
    visited = [[0] * 100 for _ in range(100)]
    s.append((x, y))
    visited[x][y] = 1

    while s:
        x, y = s.pop()
        if arr[x][y] == '3':
            return 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if arr[nx][ny] != '1' and visited[nx][ny] == 0:
                s.append((nx, ny))
                visited[nx][ny] = 1
    return 0

for tc in range(1, 11):
    N = int(input())
    res = 0
    Maze = [list(input()) for _ in range(100)]
    x, y = find_start(Maze) # (1, 1)
    res = DFS(Maze, x, y)
    print('#{} {}'.format(N, res))