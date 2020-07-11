""" グラフ関連 """

import heapq
INF = 10**18


# 単一始点最短経路 O(NlogN)
def dijkstra(N, s0, edge):

    d = [INF] * N  # 始点からの距離
    used = [False] * N  # 探索済みリスト
    edgelist = [(0, s0)]  # 始点はコスト0で初期化
    heapq.heapify(edgelist)  # ヒープにpush

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
