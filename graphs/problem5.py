import queue as Q
import math

d = {}
pi = {}

def dijkstra(G, S, T):
    for u in G:
        d[u] = math.inf 
        pi[u] = None
    for s in S:
        d[s] = 0
    q = Q.PriorityQueue()
    for u in G:
        q.put((d[u],u))
    flag = False
    u_in_T = None    
    while not q.empty() and flag == False:
        _, u  = q.get()
        print(u)
        if u in T:
           u_in_T = u         
           break      
        for v in G[u]:
            # print(u, v, d[v])
            if d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                pi[v] = u
        
    print(d, pi, d[u_in_T])




G = {'s': {'a': 2, 'b': 1},
     'a': {'s': 3, 'b': 4, 'c':8},
     'b': {'s': 4, 'a': 2, 'd': 2},
     'c': {'a': 2, 'd': 7, 't': 4},
     'd': {'b': 1, 'c': 11, 't': 4},
     't': {'c': 3, 'd': 4}}

S = ['s', 'a']
T = ['c', 't']

dijkstra(G, S, T)