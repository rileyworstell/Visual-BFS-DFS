import numpy as np
#################################
#################################
#This file is just a printed BFS
#################################
#################################

grid = []
# 9 Columns 9 C
# 9 Rows 9 R
grid = [["s", "#", "#", "#", "#", "#", "#", "#", "#", "#",]]
grid+= [["#", "#", "1", "#", "#", "#", "#", "#", "#", "#"]]
grid+= [["1", "#", "1", "#", "#", "#", "#", "#", "#", "#"]]
grid+= [["1", "#", "1", "#", "#", "#", "#", "#", "#", "#"]]
grid+= [["1", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]
grid+= [["1", "1", "1", "1", "1", "#", "#", "#", "#", "#"]]
grid+= [["#", "#", "1", "#", "1", "1", "1", "#", "#", "#"]]
grid+= [["#", "#", "1", "1", "1", "#", "1", "#", "#", "#"]]
grid+= [["#", "#", "1", "e", "#", "1", "1", "#", "#", "#"]]
grid+= [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]

R = 10
C = 10
r = 0
c = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
path = []


def bfs(s, e):
    # Do BFS staring at s
    prev = solve(s)
    # return reconstructed path from s to e
    return reconstructPath(s, e, prev)


def reconstructPath(s, e, prev):
    path = []
    path.append([prev[0][0]])
    for i in prev:
        c1 = path[-1][0][0]
        c2 = path[-1][0][1]
        b1 = i[1][0][0]
        b2 = i[1][0][1]
        if c1 == b1:
            if c2 == b2 +1 or c2 == b2 - 1:
                path.append(i[1])
        if c2 == b2:
            if c1 == b1 + 1 or c1 == b1 - 1:
                path.append(i[1])
    path.reverse()            
    print(path)
    path1 = path
    path1.pop(0)
    path1.pop(-1)
    for i in path1:
        grid[i[0][0]][i[0][1]] = "R"
    return path

def solve(s):
    r = s[0]
    c = s[1]
    q = []
    prev = []
    q.append([r,c])
    visited = np.zeros((R,C))   # Create an array of all zeros
    visited[r][c] = 1

    
    while q:
        r = q[0][0]
        c = q[0][1]
        parent = q.pop(0)

        for i in range(4):
            rr = r +dr[i]
            cc = c + dc[i]

            if rr < 0 or cc < 0: continue
            if rr >= R or cc >= C: continue
            if grid[rr][cc] == "e":
                prev.append([[rr,cc], [parent]])
                prev.pop(0)
                prev.reverse()
                #visited[rr][cc] = 2
                print("solved")
                return prev
            if grid[rr][cc] != "#": continue
            if visited[rr][cc] == 1: continue
            q.append([rr,cc])
            visited[rr][cc] = 1
            prev.append([[rr,cc], [parent]])



s = [r,c]
e = [8, 3]
bfs(s, e)



for i in grid:
        for j in i:
            print(j, end= '  ')
        print()


























