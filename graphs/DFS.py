from graph import Graph

def DFS_depth(g, u, visited):
    visited[u] = True  
    print(u, end=" ")
    for v in g[u]:
        if visited[v] == False:            
            DFS_depth(g, v, visited)            

def DFS(graph, s):
    g = graph.graph_dict
    visited = [False] * len(g)
    DFS_depth(g, s, visited) 


g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

s = 2
DFS(g, s)
