class Graph:
    graph_dict = {}

    def addEdge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        else:
            self.graph_dict[node].append(neighbour)
    
    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print(node,": ", neighbour)
    

# g = Graph()
# g.addEdge(0, 1) 
# g.addEdge(0, 2) 
# g.addEdge(1, 2) 
# g.addEdge(2, 0) 
# g.addEdge(2, 3) 
# g.addEdge(3, 3) 

# g.show_edges()
