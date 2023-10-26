import Graph 
import functools
from Solution import Solution

class Magician(Solution):
    '''
    Class to solve the following problem:
    
    A state consists of N cities numbered from 0 to N-1. All the roads in the state are bidirectional. Each city is connected to 
    another city by one direct road only. A magician travels to these cities to perform shows. He knows a magic spell that can 
    completely eliminate the distance between any two directly connected cities. But he must be very careful because this magic 
    spell can be performed only K number of times.

    Write an algorithm to find the length of the shortest route between two given cities after performing the magic spell K number
    of times. The output is -1 if no path exists.
    '''
    def __init__(self):
        super().__init__() 
    
    def solution(self, N: int, A: int, B: int, K: int, P:list[list[int]]) -> None:
        '''
        Return solution to the magician problem.
        Parameters
        ----------
        N : int, number of cities
        A : int, source city
        B : int, target city
        K : int, number of spells
        P : List[e = List[int]], list between bidirectional edge between e[0] and e[1] with weight e[2]
                
        Returns
        -------
        dp(A,B,K,N) : int, total weight of the shortest path between A and B after performing K spells
        '''
        g = Graph.Graph(N)
        for x in P:
            g.addEdge(x[0],x[1],x[2])
        
        @functools.lru_cache(maxsize=None)
        def dp(i,j,k,n):
            if k == 0: # Base case
                return g.bellmanFord(i)[j] # Minimum cost from i to j without using spells
            else:
                path = dp(i,j,0,N-1)
                for l in range(N):
                    if g.adjMatrix[i][l] == 1 and n > 0:
                        path = min( path, dp(l,j,k-1,n-1), dp(i,l,0,n-1) + dp(l,j,k,n-1)) # DP recurrence equation

            return path
        
        self.setSolution(dp(A,B,K,N-1))

    def solution2(self, N: int, A: int, B: int, K: int, P:list[list[int]]) -> None:
        '''
        Return solution to the magician problem without relying on the class Graph.

        Parameters
        ----------
        N : int, number of cities
        A : int, source city
        B : int, target city
        K : int, number of spells
        P : List[e = List[int]], list between bidirectional edge between e[0] and e[1] with weight e[2]
                
        Returns
        -------
        dp(A,B,K,N) : int, total weight of the shortest path between A and B after performing K spells
        '''
        
        graph = []
        adjMatrix = [[0]*N for _ in range(N)]
        for x in P:
            graph.append([x[0],x[1],x[2]])
            graph.append([x[1],x[0],x[2]])
            adjMatrix[x[0]][x[1]] = 1
            adjMatrix[x[1]][x[0]] = 1

        costMatrix = []
        # Bellman-Ford algorithm
        for i in range(N):
            # Initialise with i being the source vertex
            dist = [float("Inf")] * N
            dist[i] = 0

            # Iterate
            for _ in range(N- 1):
                terminate = True
                for u, v, w in graph:
                    if dist[v] != float("Inf") and dist[v] + w < dist[u]:
                        terminate = False
                        dist[u] = dist[v] + w
                if terminate == True:
                    break
            costMatrix.append(dist)


        # Use a DP approach to complete problem
        @functools.lru_cache(maxsize=None)
        def dp(i,j,k,n):
            if k == 0: # Base case
                return costMatrix[i][j] # Minimum cost from i to j without using spells
            else:
                path = dp(i,j,0,N-1)
                for l in range(N):
                    if adjMatrix[i][l] == 1 and n > 0:
                        path = min( path, dp(l,j,k-1,n-1), costMatrix[i][l] + dp(l,j,k,n-1)) # DP recurrence equation

            return path
        
        self.setSolution(dp(A,B,K,N-1))