from collections import defaultdict


class Graph:
    def __init__(self):
        # Need to figure out the use for this later
        self.edges = set()
        # Creating graph as adjacency list
        # 0: [1,2] Here 0 is connected to 1 and 2
        self.graph = defaultdict(list)
        self.visited = []

    # Adds an edge u -> v to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.visited = [False] * len(self.graph)

    def DFS(self, startNode):
        self.visited[startNode] = True
        print(startNode)
        for node in self.graph[startNode]:
            if not self.visited[node]:
                self.DFS(node)


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
g.DFS(2)
