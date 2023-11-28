from collections import defaultdict

class Graph:
    """
    A class to represent a graph.

    ...

    Attributes
    ----------
    vertices : int
        number of vertices
    directed : bool
        stating if the graph is undirected or not
    adjMatrix : List[List[int]]
        adjacency matrix

    Methods
    -------
    addEdge(u,v,w):
        adds an edge with weight w between u and v
    bellmanFord(src):
        Computes the shortest distance from each vertex to  
        src via the Bellman-Ford algorithm.
    """

    def __init__(self, vertices: int, directed=False):
        """
        Constructs all the necessary attributes for the graph object.

        Parameters
        ----------
            vertices : int
                number of vertices
            directed : bool
                stating if the graph is undirected or not
        """
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)
        self.d = directed # Checking if the graph is undirected or not

        self.adjMatrix = []
        for _ in range(vertices):
            self.adjMatrix.append([0 for __ in range(vertices)])
 
    def addEdge(self, u: int, v: int, w: float) -> None:
        '''
        Adds an edge between vertices.

        Parameters
        ----------
        u : first vertex
        u : second vertex
        w : weighted edge between first and second vertex
            
        Returns
        -------
        None
        '''

        if self.d == False:
            self.graph[u].append([v, w])
            self.graph[v].append([u, w])
            self.adjMatrix[u][v] = 1
            self.adjMatrix[v][u] = 1
        else:
            self.graph[u].append([v, w])
            self.adjMatrix[u][v] = 1

    def DFSUtil(self, v = int, visited = set) -> None:
        '''
        Function called recursively by DFS

        Parameters
        ----------
        v       : vertex
        visited : set of visited vertices
            
        Returns
        -------
        None
        '''
 
        # Mark the current node as visited
        visited.add(v)
 
        # Recur for all the adjacent vertices
        for adjacentVertex, w in self.graph[v]:
            if adjacentVertex not in visited:
                self.DFSUtil(adjacentVertex, visited)

    def DFS(self, v: int) -> set:
        '''
        Function to perform DFS starting from vertex v

        Parameters
        ----------
        v       : vertex
            
        Returns
        -------
        set of vertices accessible via v
        '''
 
        # set for visited vertices
        visited = set()
 
        # Call the recursive helper function
        self.DFSUtil(v, visited)

        return visited
    
    def bellmanFord(self, src: int) -> list[int]:
        '''
        Computes the shortest distance from each vertex to the 
        source vertex via the Bellman-Ford algorithm.

        Parameters
        ----------
        u : source vertex
            
        Returns
        -------
        dist : shortest paths from each vertex to the source
        '''

        # Initialise
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Iterate
        for _ in range(self.V - 1):
            terminate = True
            for vert in self.graph:
                for adjacentVert, weightedEdge in self.graph[vert]:
                    if dist[adjacentVert] != float("Inf")\
                          and dist[adjacentVert] + weightedEdge < dist[vert]:
                        terminate = False
                        dist[vert] = dist[adjacentVert] + weightedEdge
            if terminate == True:
                break
        return dist
    
