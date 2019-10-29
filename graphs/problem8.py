def dijkstra(G, S, T):
    for u in G:
        d[u] = math.inf 
        pi[u] = None
    for s in S:
        d[s] = 0
    q = Q.PriorityQueue()
    for u in G:
        q.put((d[u],u))
    while not q.empty():
        _, u  = q.get()
        print(u)       
        for v in G[u]:
            if d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                pi[v] = u
            # if v in T:
            #     break                
    return pi, d

G = {'s': {'a': 0.2, 'b': 0.1},
     'a': {'s': 0.3, 'b': 0.4, 'c':0.8},
     'b': {'s': 0.4, 'a': 0.2, 'd': 0.2},
     'c': {'a': 0.2, 'd': 0.7, 't': 0.4},
     'd': {'b': 0.1, 'c': 0.11, 't': 0.5},
     't': {'c': 0.3, 'd': 0.5}}

def graph_update(G)
    for u in 