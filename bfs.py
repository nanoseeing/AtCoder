""" 幅優先探索 """

from collections import deque


# グラフ探索（基本形）
def bfs(N, v0, edge):

    search = [True] * N
    search[v0] = False
    q = deque()
    q.append(v0)

    while q:
        v = q.popleft()
        for nv in edge[v]:
            if search[nv]:
                q.append(nv)
                search[nv] = False


# グリッド移動
def bfs_grid(H, W, sx, sy, grid):

    q = deque()
    q.append((sx, sy))
    d = [[-1 for _ in range(W)] for _ in range(H)]
    d[sy][sx] = 0
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        now = q.popleft()
        x, y = now
        for m in move:
            n_x, n_y = x + m[0], y + m[1]
            if (0 <= n_x and n_x < W) and (0 <= n_y and n_y < H):
                if d[n_y][n_x] == -1 and grid[n_y][n_x] == '.':
                    d[n_y][n_x] = d[y][x] + 1
                    q.append((n_x, n_y))


# 閉路検出
def judge_tree(N, v0, edge):

    search = [True] * N
    search[v0] = False
    q = deque()
    q.append((v0, -1))

    while q:
        v, pv = q.popleft()
        for nv in edge[v]:
            if search[nv]:
                q.append((nv, v))
                search[nv] = False
            elif pv != nv:
                return True

    return False
