from collections import deque

#####################################################################
def inputCheck(num, min, max, msg=''): #부적절한 입력 방지
    while 1:
        data = input(msg).split()
        err = 0
        res = []
        if len(data) != num: err = 1
        else:
            for i in data:
                if not i.isdigit() or int(i) < min or int(i) > max:
                    err = 1
                    break
                res.append(int(i))
        if err == 1: print("올바르지 않은 입력입니다.")
        else: return res

def bfs(): #미로 탐색
    q = deque([(start_y, start_x)])
    v[start_y][start_x] = 1

    if (start_y, start_x) == (end_y, end_x):
        return 0 #시작점 = 도착점

    while q:
        y, x = q.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ny, nx = y+dy, x+dx
            if 0<=ny<h and 0<=nx<w and g[ny][nx] and not v[ny][nx]:
                g[ny][nx] = g[y][x] + 1
                v[ny][nx] = 1
                q.append((ny, nx))
                trace.append([(y, x), (ny, nx)])
                if (end_y, end_x) == (ny, nx): break
        if (end_y, end_x) == (ny, nx): break
    
    if g[end_y][end_x]==1:
        return -1 #미로 해답 없음
    
    from_y, from_x = trace[-1][0]
    for from_xy, to_xy in trace[::-1]:
        to_y, to_x = to_xy
        if from_x==to_x and from_y==to_y:
            from_y, from_x = from_xy
            path.append(to_xy)

    # https://velog.io/@1ncursio/A-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%EA%B5%AC%ED%98%84%ED%95%B4%EB%B3%B4%EC%9E%90-Python3
    # 탐색한 경로들로부터 최단 경로를 찾아내는 코드 참조

    return g[end_y][end_x] - 1 #최단 경로

def print_maze():
    print("[ 미로 구조 ]")
    for i in range(h):
        for j in range(w):
            if (i, j) == (start_y, start_x): print("S", end=" ")
            elif (i, j) == (end_y, end_x): print("G", end=" ")
            elif g[i][j]: print("□", end=" ")
            else: print(".", end=" ")
        print()
    print()

def print_visit():
    print("[ 방문한 길 ]")
    for i in range(h):
        for j in range(w):
            if (i, j) == (start_y, start_x): print("S", end=" ")
            elif (i, j) == (end_y, end_x): print("G", end=" ")
            elif v[i][j]: print("■", end=" ")
            elif g[i][j]: print("□", end=" ")
            else: print(".", end=" ")
        print()
    print()

def print_shortest_path():
    print("[ 최단 경로 ]")
    for i in range(h):
        for j in range(w):
            if (i, j) == (start_y, start_x): print("S", end=" ")
            elif (i, j) == (end_y, end_x): print("G", end=" ")
            elif (i, j) in path: print("■", end=" ")
            elif g[i][j]: print("□", end=" ")
            else: print(".", end=" ")
        print()
    print()
#####################################################################

print("[ 미로 탐색 알고리즘 ]")
w, h = inputCheck(2, 2, 100, "미로의 가로, 세로의 길이를 순서대로 입력 (띄어쓰기로 구분) : ")

print(f"{w}x{h} 크기의 미로 입력 [벽: 0, 길: 1] (띄어쓰기로 구분)")
g = [ inputCheck(w, 0, 1, f"{i+1:02d}" + "번째 줄 : ") for i in range(h) ]
v = [ [0]*w for _ in range(h) ]
trace, path = [], []

while 1:
    start_x, start_y = inputCheck(2, 0, 100, "시작점의 x, y좌표 입력 (띄어쓰기로 구분) : ")
    if start_x >= w or start_y >= h: print("해당 좌표는 미로 내의 좌표가 아닙니다.")
    elif not g[start_y][start_x]: print("해당 좌표는 길이 아닙니다.")
    else: break
while 1:
    end_x, end_y = inputCheck(2, 0, 100, "도착점의 x, y좌표 입력 (띄어쓰기로 구분) : ")
    if end_x >= w or end_y >= h: print("해당 좌표는 미로 내의 좌표가 아닙니다.")
    elif not g[end_y][end_x]: print("해당 좌표는 길이 아닙니다.")
    else: break

print("\n경로 탐색을 진행합니다.\n")
result = bfs()

print_maze()
print_visit()

if result == -1:
    print("미로의 해답이 존재하지 않습니다.\n")
    print("최단 거리: 없음")
else:
    print_shortest_path()
    print("최단 거리:", result)