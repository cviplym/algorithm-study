"""
Source
- Tistory: https://codepractice.tistory.com/81

1) 아이디어
- 이중 for문으로 board 탐색
- 범위를 벗어나거나 이미 방문한 칸이 나오면 방향 전환
- SPACING 간격으로 숫자 채우고 나머지는 0으로 채움

2) 시간 복잡도
- O(N^2) (모든 칸을 정확히 한 번씩 방문)
- 최대 연산: N^2 = 225 (최대 N이 15)

3) 자료구조
- board: int[][]
    - -1: 미방문
"""

import sys
input = sys.stdin.readline

# 터미널에서 실행되는 경우에만 실행
if sys.stdin.isatty():
    print("입력:", end=" ", flush=True)

N = int(input())

# 결과 배열 (-1: 미방문)
board = [[-1] * N for _ in range(N)]

# 달팽이 모양으로 채우는 간격
SPACING = 2

# 방향 (0: 우, 1: 하, 2: 좌, 3: 상)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
d = 0 # 현재 방향 

py, px = 0, 0 # 현재 위치

num = 0  # 채워지는 숫자
step = 0 # 방문 순서

# 총 N^2 칸을 차례대로 방문
for step in range(N * N):
    # 현재 위치에 숫자 채우기
    if step % SPACING == 0:
        num += 1
        board[py][px] = num
    else: 
        board[py][px] = 0

    # 다음 위치 계산
    ny = py + dy[d]
    nx = px + dx[d]

    # 다음 위치가 범위 밖이거나 이미 방문한 경우 방향 전환
    if not (0 <= ny < N and 0 <= nx < N and board[ny][nx] < 0):
        d = (d + 1) % 4
        ny = py + dy[d]
        nx = px + dx[d]

    py, px = ny, nx # 현재 위치 업데이트

# 결과 출력
for y in range(N):
    for x in range(N):
        print(f"{board[y][x]:02d}", end=" ")
    print()

    


    


