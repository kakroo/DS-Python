from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, startNode):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(startNode)
        visited[startNode] = True
        while queue:
            start = queue.pop()
            print(start)
            for node in self.graph[start]:
                if visited[node] == False:
                    queue.append(node)
                    visited[start] = True


# Create a graph given
# in the above diagram
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print("Following is DFS from (starting from vertex 2)")
g.BFS(2)
