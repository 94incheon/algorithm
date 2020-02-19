# dfs 함수 생성 ( 재귀버전 )
def dfs(x, y):
    if maze[x][y] == '3': # 목적지에 도착했으면 1 리턴
        return 1
    else:
        maze[x][y] = '1' # 방문한 칸을 벽으로 채운다.
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if maze[nx][ny] != '1': # 벽이 아닌 칸이 있으면
                if dfs(nx, ny) == 1: # 이동, 목적지를 찾은 경우 중단
                    return 1
        return 0
    
########################################################################################

# dfs 함수 생성 ( 반복문 버전 )
def dfs2(x, y):
    s = []
    visited = [[0]*16 for _ in range(16)]
    s.append((x, y)) # 좌표를 묶어서 넣을 것
    visited[x][y] = 1
    while s: # 스택이 있으면 반복해라
        x, y = s.pop()
        if maze[x][y] == '3': # 목적지에 다다르면 중단
            return 1
        for k in range(4): # 4방향으로
            nx = x + dx[k] # 주변칸에
            ny = y + dy[k]
            if maze[nx][ny] != '1' and visited[nx][ny] == 0 : # 벽이 아니고 방문안한 칸이 있으면,
                s.append((nx, ny)) # 방문할 칸 목록에 push
                visited[nx][ny] = 1
    return 0 # 반복을 다 돌고 결과가 없었으면 0

################################################################################################

dx = [0, 1, 0, -1] # 우 하 좌 상 ( 시계 방향 )
dy = [1, 0, -1, 0] 
for tc in range(1, 11):
    T = int(input())
    # 미로 생성
    maze = [list(input()) for _ in range(16)]

    # 시작위치
    si, sj = -1, -1 
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                si, sj = i, j
                break
        if si != -1:
            break

    r = dfs(si, sj)
    print('#{} {}'.format(T, r))