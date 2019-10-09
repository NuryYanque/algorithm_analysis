from graph import Graph

g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(2, 1) 
g.addEdge(3, 2) 
g.addEdge(4, 3) 
g.addEdge(4, 5)
g.addEdge(5, 5)

WHITE = 1
GRAY = 2
BLACK = 3

num_V = len(g.graph_dict)
color = [WHITE] * num_V
pi = [None] * num_V
d = [-1] * num_V
f = [-1] * num_V

time = 0

def DFS_visit(g, u):
    color[u] = GRAY
    global time
    time += 1
    d[u] = time
    
    for v in g[u]:
        if color[v] == WHITE:
            pi[v] = u            
            DFS_visit(g, v)
    color[u] = BLACK
    f[u] = time = time + 1

def DFS(g):   
    
    global time
    time  = 0

    for u in g:
        if color[u] == WHITE:
            DFS_visit(g, u)


# s = 2
DFS(g.graph_dict)
print(d)
print(f)

def print_path(s, v):    
    if s == v:        
        print(s, end=' ')
    elif pi[v] == None:
        print('No path from', s, 'to', v, 'exist')
    else:
        print_path(s, pi[v])
        print(v, end=' ')

print_path(4, 5)
