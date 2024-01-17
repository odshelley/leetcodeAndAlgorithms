from collections import defaultdict

class Graph:
    """
    A class to represent a graph.

    ...

    Attributes
    ----------
    vertices : int
        number of vertices
    isDirected : bool
        stating if the graph is unisDirected or not
    adjMatrix : List[List[int]]
        adjacency matrix

    Methods
    -------
    addEdge(u,v,w):
        adds an edge with weight w between u and v
    findPaths(src,trgt):
        Finds all paths from src to trgt vertex using DFS
    DFS(src):
        Finds all vertices accessible from src via DFS
    BFS(src):
        Finds all vertices accessible from src via BFS
    bellmanFord(src):
        Computes the shortest distance from each vertex to  
        src via the Bellman-Ford algorithm
    """

    def __init__(self, vertices: int, directed=False):
        """
        Constructs all the necessary attributes for the graph object.

        Parameters:
            vertices (int): number of vertices
            isDirected (bool): stating if the graph is unisDirected or not

        Returns:
            None
        """
        self.numberOfVertices = vertices  # No. of vertices
        self.graph = defaultdict(list)
        self.isDirected = directed # Checking if the graph is unisDirected or not

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

        if self.isDirected == False:
            self.graph[u].append([v, w])
            self.graph[v].append([u, w])
            self.adjMatrix[u][v] = 1
            self.adjMatrix[v][u] = 1
        else:
            self.graph[u].append([v, w])
            self.adjMatrix[u][v] = 1

    def DFSHelper(self, v = int, visited = set) -> None:
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
                self.DFSHelper(adjacentVertex, visited)

    def DFS(self, v: int) -> set:
        '''
        Function to perform DFS starting from vertex v

        Parameters
        ----------
        v : vertex
            
        Returns
        -------
        set of vertices accessible via v
        '''
 
        # set for visited vertices
        visited = set()
 
        # Call the recursive helper function
        self.DFSHelper(v, visited)

        return visited
    
    def BFS(self, v: int) -> set:
        '''
        Function to perform BFS starting from vertex v

        Parameters
        ----------
        v : vertex
            
        Returns
        -------
        set of vertices accessible via v
        '''
 
        # Mark all the vertices as not visited
        visited = [False] * self.numberOfVertices
 
        # Create a queue for BFS
        queue = []
        visited_from_v = set()
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(v)
        visited[v] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            v = queue.pop(0)
            visited_from_v.add(v)
 
            # Get all adjacent vertices of the
            # dequeued vertex s.
            # If an adjacent has not been visited,
            # then mark it visited and enqueue it
            for adjacentVertex, w in self.graph[v]:
                if visited[adjacentVertex] == False:
                    queue.append(adjacentVertex)
                    visited[adjacentVertex] = True
        
        return visited_from_v
    
    def pathHelper(self, source: int, target: int, visited: list, path: list, collection: list) -> None:
        '''
        Function to perform DFS starting from vertex v

        Parameters
        ----------
        source     : source vertex
        target     : target vertex
        visited    : list of visited vertices
        path       : current path
        collection : collection of paths
            
        Returns
        -------
        updates the paths from src to trgt
        '''
 
        visited[source] = True # Mark current node as visited 
        path.append(source) # update path
 
        if source == target:
            collection.append(path.copy()) # If source vertex is same as target, add paths to collection
        else:
            # Recur for all the vertices adjacent to this vertex
            for vertex, weight in self.graph[source]:
                if visited[vertex]== False:
                    self.pathHelper(vertex, target, visited, path, collection)
                     
        path.pop() # Remove current vertex 
        visited[source]= False # mark it as unvisited
  
    def findPaths(self, source: int, target: int) -> list[list[int]]:
        '''
        Find all paths from source to target vertex

        Parameters
        ----------
        source     : source vertex
        target     : target vertex
            
        Returns
        -------
        list of all paths from source to target vertex
        '''

        visited =[False]*(self.numberOfVertices) # Mark all the vertices as not visited
        path = [] # Create an array to store current path
        collection = [] # Create an array to store paths
 
        # Call helper function
        self.pathHelper(source, target, visited, path, collection)

        return collection
    
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
        dist = [float("Inf")] * self.numberOfVertices
        dist[src] = 0

        # Iterate
        for _ in range(self.numberOfVertices - 1):
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
    
