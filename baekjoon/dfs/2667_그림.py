'''
[Source]
- BOJ 2667 그림: https://www.acmicpc.net/problem/2667

[References]
- YouTube: https://www.youtube.com/watch?v=3_eVkTkBbJE&list=PLi-xJrVzQaxXC2Aausv_6mlOZZ2g2J6YB&index=3

1. 아이디어
- 2중 for문 돌면서 1인 값 찾기 & 크기 DFS로 탐색
- list에 각 크기 넣고 sort한 후 출력

2. 시간 복잡도
- DFS: O(V+E)
- V: 25^2 / E: 4 x 25^2
- V + E = 5 x 625 < 35000 >> 통과

3. 데이터 구조
- 입력 행렬: int[][]
- 체크 행렬: bool[][]

'''
import sys
input = sys.stdin.readline

N = int(input())
boarder = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False]*N for _ in range(N)]

each = 0
home_list = []

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<N:
            if boarder[ny][nx]==1 and not chk[ny][nx]:
                chk[ny][nx] = True
                dfs(ny, nx)

for j in range(N):
    for i in range(N):
        if boarder[j][i]==1 and not chk[j][i]:
            chk[j][i] = True
            each = 0
            dfs(j, i)
            home_list.append(each)

home_list.sort()
print(len(home_list))
for home in home_list:
    print(home)
      
