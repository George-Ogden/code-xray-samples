import heapq as hq
import math
from dataclasses import dataclass


@dataclass
class Edge:
    target: int
    weight: float


# Modified from https://stackoverflow.com/a/56740241/12103577.
def dijkstra(G: list[list[Edge]], source):
    n = len(G)
    visited = [False] * n
    weights = [math.inf] * n
    paths = [None] * n
    queue = []

    weights[source] = 0
    hq.heappush(queue, (0, source))

    while queue:
        current_weight, u = hq.heappop(queue)

        if visited[u]:
            continue

        visited[u] = True

        for edge in G[u]:
            if not visited[edge.target]:
                new_weight = current_weight + edge.weight
                if new_weight < weights[edge.target]:
                    weights[edge.target] = new_weight
                    paths[edge.target] = u
                    hq.heappush(queue, (new_weight, edge.target))

    return paths, weights
