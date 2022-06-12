import queue as Q
import math

G = {'s': {'a': -(math.log(0.3)), 'b': -(math.log(0.5))},
     'a': {'s': -(math.log(0.4)), 'b': -(math.log(0.1)), 'c':-(math.log(0.9))},
     'b': {'s': -(math.log(0.7)), 'a': -(math.log(0.4)), 'd': -(math.log(0.2))},
     'c': {'a': -(math.log(0.8)), 'd': -(math.log(0.7)), 't': -(math.log(0.4))},
     'd': {'b': -(math.log(0.1)), 'c': -(math.log(0.9)), 't': -(math.log(0.4))},
     't': {'c': -(math.log(1)), 'd': -(math.log(0.2))}}

d = {}
pi = {}

def dijkstra(G, s, t):
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
            # print(u, v, d[v])
            if d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                pi[v] = u
                q.put((d[v],v))
    path = [t]
    while pi[t] != None:
        path.append(pi[t])
        t = pi[t]
    print(path)
    return reversed(path)

a = dijkstra(G, 'd', 'b')
print(list(a))

# # print(G)
# dist = dijkstra(G, 's', 'd')
# print(dist)