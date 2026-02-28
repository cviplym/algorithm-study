'''
[Soure] 
- BOJ 1926 그림: https://www.acmicpc.net/problem/1926

[References]
- YouTube: https://www.youtube.com/watch?v=ansd5B27uJM&list=PLi-xJrVzQaxXC2Aausv_6mlOZZ2g2J6YB&index=2

1. 아이디어
- 2중 for => 값 1 && 방문 X => BFS
- BFS 돌면서 그림 개수 +1, 최댓값을 갱신

2. 시간복잡도
- BFS: O(V + E)
- V: m x n (500 x 500)
- E: 4 x m x n (500 x 500)
- V + E: 5 * 250,000 = 1,250,000 < 2 => 가능

3. 자료구조
- 그래프 전체 진도 : int[][]
- 방문: bool[][]
- Queue(BFS)
'''

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
boarder = [list(map(int, input().split())) for _ in range(n)]
chk = [[False]*m for _ in range(n)]

cnt = 0
max_v = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(y,x):
    rs = 1
    q = deque()
    q.append((y,x))
    
    while q:
        py, px = q.popleft()
        for k in range(4):
            ny = py + dy[k]
            nx = px + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if boarder[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    rs +=1
                    q.append((ny, nx))
    return rs
                    
    

for j in range(n):
    for i in range(m):
        if boarder[j][i] == 1 and chk[j][i] == False:
            cnt += 1
            chk[j][i] = True
            max_v = max(max_v, bfs(j, i))
                        
 #
print(cnt)
print(max_v)
