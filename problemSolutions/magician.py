import Graph 
import functools

class Solution:
    '''
    Class to solve the following problem:
    
    A state consists of N cities numbered from 0 to N-1. All the roads in the state are bidirectional. Each city is connected to another city by one direct road only. A magician travels to these cities to perform shows. He knows a magic spell that can completely eliminate the distance between any two directly connected cities. But he must be very careful because this magic spell can be performed only K number of times.

    Write an algorithm to find the length of the shortest route between two given cities after performing the magic spell K number of times. The output is -1 if no path exists.
    '''
    def __init__(self):
        self.answer = None
    
    def magician(self, N: int, A: int, B: int, K: int, P:list[list[int]]) -> int:
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
                path = dp(i,j,0,N)
                for l in range(N):
                    if g.adjMatrix[i][l] == 1 and n > 0:
                        path = min( path, dp(l,j,k-1,n-1), dp(i,l,0,n-1) + dp(l,j,k,n-1)) # DP recurrence equation

            return path
        
        self.answer = dp(A,B,K,N)