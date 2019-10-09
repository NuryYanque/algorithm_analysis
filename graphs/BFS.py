from graph import Graph
from queue import Queue
import math

WHITE = 1
GRAY = 2
BLACK = 3

def BFS(G, s):
    num_V = len(G.graph_dict)

    color = [WHITE] * num_V
    d = [math.inf] * num_V
    pi = [None] * num_V 

    color[s] = GRAY
    d[s] = 0
    pi[s] = None

    Q = Queue()
    Q.put(s)

    while not Q.empty():
        # Deque
        u = Q.get()
        
        # Get adjanced vertices from deque vertex u 
        for v in G.graph_dict[u]:
            # if adjanced vertex has not been visited
            if color[v] == WHITE:
                color[v] = GRAY
                d[v] = d[u] + 1
                pi[v] = u
                Q.put(v)
        color[u] = BLACK
    return pi


g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

s = 0
pi = BFS(g, s)
print(pi)

def print_path(s, v):    
    if s == v:        
        print(s, end=' ')
    elif pi[v] == None:
        print('No path from', s, 'to', v, 'exist')
    else:
        print_path(s, pi[v])
        print(v, end=' ')

dfs_tree = print_path(s, 3)
print(dfs_tree)