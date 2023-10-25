import unittest

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

    def __init__(self, vertices, directed=False):
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
        self.graph = []
        self.d = directed # Checking if the graph is undirected or not

        self.adjMatrix = []
        for _ in range(vertices):
            self.adjMatrix.append([0 for __ in range(vertices)])
 
    def addEdge(self, u, v, w):
        '''
        Adds an edge between vertices.

        Parameters
        ----------
        u : int, first vertex
        u : int, second vertex
        w : float, weighted edge between first and second vertex
            
        Returns
        -------
        None
        '''

        if self.d == False:
            self.graph.append([u, v, w])
            self.graph.append([v, u, w])
            self.adjMatrix[u][v] = 1
            self.adjMatrix[v][u] = 1
        else:
            self.graph.append([u, v, w])
            self.adjMatrix[u][v] = 1
    
    def bellmanFord(self, src):
        '''
        Computes the shortest distance from each vertex to the 
        source vertex via the Bellman-Ford algorithm.

        Parameters
        ----------
        u : int, source vertex
            
        Returns
        -------
        dist : List, shortest paths from each vertex to the source
        '''

        # Initialise
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Iterate
        for _ in range(self.V - 1):
            terminate = True
            for u, v, w in self.graph:
                if dist[v] != float("Inf") and dist[v] + w < dist[u]:
                    terminate = False
                    dist[u] = dist[v] + w
            if terminate == True:
                break
        return dist
    
class TestGraph(unittest.TestCase):

    def testBellmanFord(self):
        """ensures that the Bellman Ford algorithm works."""

        g = Graph(5,True)
        g.addEdge(1,0,1)
        g.addEdge(2,0,3)
        g.addEdge(1,2,2)
        g.addEdge(2,1,1)
        g.addEdge(3,1,8)
        g.addEdge(4,2,2)
        g.addEdge(3,4,4)
        g.addEdge(4,3,2)

        self.assertEqual(g.BellmanFord(0), [0, 1, 2, 8, 4], "incorrect distances")
        


    
    
