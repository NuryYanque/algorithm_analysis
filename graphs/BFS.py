from graph import Graph
from queue import Queue

def BFS(graph, s): 
    
    # Mark all the vertices as not visited
    visited = [False] * (len(graph.graph_dict))
    
    Q = Queue()
    Q.put(s)

    visited[s] = True

    while not Q.empty():
        # Deque
        u = Q.get()
        print(u, end=" ")
        # Get adjanced vertices from deque vertex u 
        for v in graph.graph_dict[u]:
            # if adjanced vertex has not been visited
            if visited[v] == False:
                # mark as visited
                visited[v] = True
                # enqueue it
                Q.put(v)    

g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

s = 2
path = BFS(g, s)
print(path)