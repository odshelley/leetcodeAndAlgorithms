from Solution import Solution
import functools

class Triangle(Solution):
    '''
    This class is to solve the following Leetcode problem:

    Given a triangle array, return the minimum path sum from top to bottom.

    For each step, you may move to an adjacent number of the row below. More formally, if you are on 
    index i on the current row, you may move to either index i or index i + 1 on the next row.
    '''

    def __init__(self):
        super().__init__()
    
    def solution(self, triangle: list[list[int]]) -> None:
        '''
        Parameters
        ----------
        triangle : the triangle in question
            
        Returns
        -------
        updates answer to be the minimum cost path
        '''

        @functools.lru_cache()
        def dp(i,j):
            # Base case
            if i == 0 and j == 0:
                return triangle[i][j]
                
            # DP recursion
            minimum = float('inf')
            if j == 0:
                minimum = triangle[i][j] + dp(i-1,j)
            elif j == i:
                minimum = triangle[i][j] + dp(i-1,j-1)
            else:
                minimum = min(triangle[i][j] + dp(i-1,j-1),triangle[i][j] + dp(i-1,j))
        
            return minimum 

        result = float('inf')

        for i in range(len(triangle)):
            result = min(result, dp(len(triangle)-1,i))

        self.setSolution(result)
