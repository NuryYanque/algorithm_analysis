from graph import Graph
from DFS import DFS
from collections import OrderedDict

def build_G_r(G):
    G_r = {}
    for u in G:
        if u not in G_r:
            G_r[u] = []      
        for v in G[u]:
            if v not in G_r:
                G_r[v] = []
                G_r[v].append(u)
            else:
                G_r[v].append(u)
    return G_r

def kosaraju_shamir(G):
    # DFS on G
    f, _ = DFS(G)
    for k,v in f.items():
        print(k, v, end='\t')
    print()
    # f in decrease order
    f_sorted = OrderedDict(sorted(f.items(), key=lambda kv: kv[1], reverse=True))
    for k,v in f_sorted.items():
        print(k, v, end='\t')
    print()
    # Build G_r, it is G inverted edges
    G_r = build_G_r(G) 
    for k,v in G_r.items():
        print(k, v)
    print()
    # G_r in orden on f descrease order
    G_r_sorted = OrderedDict([(k, G_r[k]) for k,v in f_sorted.items()])
    for k,v in G_r_sorted.items():
        print(k, v)
    # DFS on G_r
    _, pi = DFS(G_r_sorted)

    # components
    print(pi)

graph = {'a': ['b', 'g'],
         'b': ['c', 'f'],  
         'c': ['b', 'd'],  
         'd': ['e'], 
         'e': ['d'], 
         'f': ['c'],
         'g': ['h', 'i'], 
         'h': ['d', 'g', 'j'],
         'i': ['h'],
         'j': []}


# g.show_edges()

kosaraju_shamir(graph)