""" グラフ関連 """

from collections import deque
import heapq
INF = 10**18


# 最短経路（BFS）O(V+E)
def bfs(N, v0, edge):

    d = [-1] * N
    d[v0] = 0
    q = deque()
    q.append(v0)

    while q:
        v = q.popleft()
        for nv in edge[v]:
            if d[nv] == -1:
                q.append(nv)
                d[nv] = d[v] + 1

    return d


# トポロジカルソート O(V+E)
def topological_sort(N, dag):

    degree = [0] * N
    for i in range(N):
        for v in dag[i]:
            degree[v] += 1

    ret = [v for v in range(N) if degree[v] == 0]
    q = deque(ret)

    while q:
        v = q.popleft()
        for nv in dag[v]:
            degree[nv] -= 1
            if degree[nv] == 0:
                q.append(nv)
                ret.append(nv)

    return ret


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


# 単一始点最短経路 O(NlogN)
def dijkstra(N, s0, edge):

    d = [INF] * N
    used = [False] * N
    edgelist = [(0, s0)]
    heapq.heapify(edgelist)

    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = True
        for e in edge[v]:
            if d[e[1]] <= (e[0] + d[v]) or used[e[1]]:
                continue
            heapq.heappush(edgelist, [e[0] + d[v], e[1]])
    return d


# 全点対間最短経路(ワーシャルフロイド) O(V^3)
cost = [[INF for _ in range(N)] for _ in range(N)]
for i in range(N):
    cost[i][i] = 0


def warshall_floyd(N, cost):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if cost[i][k] < INF and cost[k][j] < INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
