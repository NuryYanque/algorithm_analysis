import queue as Q
import math

d = {}
pi = {}

def dijkstra(G, s):
    for u in G:
        d[u] = math.inf 
        pi[u] = None
    d[s] = 0
    q = Q.PriorityQueue()
    for u in G:
        q.put((d[u],u))
    while not q.empty():
        _, u  = q.get()           
        for v in G[u]:
            if d[v] > d[u] + G[u][v]:
                pi[v] = u
                d[v] = d[u] + G[u][v]
    return pi, d



graph = {'s': {'a': 2, 'b': 1},
         'a': {'s': 3, 'b': 4, 'c':8},
         'b': {'s': 4, 'a': 2, 'd': 2},
         'c': {'a': 2, 'd': 7, 't': 4},
         'd': {'b': 1, 'c': 11, 't': 5},
         't': {'c': 3, 'd': 5}}

pi, d = dijkstra(graph, 's')

print(pi)
print(d)