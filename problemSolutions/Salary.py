from Solution import Solution 
import functools

class Salary(Solution):
    '''
    Class to solve the following problem:

    Stephen is doing an internship in a company for N days. Each day, he may choose either an easy task or a difficult task. 
    He may also choose to perform no task at all. He chooses a difficult task on days when and only when he did not perform 
    any work the previous day. The amount paid by the company for both the easy and difficult tasks can vary each day, but 
    the company always pays more for difficult tasks.

    Write an algorithm to help Stephen earn the maximum salary. 
    '''
    def __init__(self):
        super().__init__() 
    
    def solution(self, N: int, M: int, P: list[list[int]]) -> None:

        assert(M == len(P[0]))
        assert(N == len(P))

        @functools.lru_cache(maxsize=None)
        def dp(i,k):
            if i == N-1:
                if k == 0:
                    return P[N-1][1]
                else:
                    return P[N-1][0]
            else:
                if k == 0:
                    pay = max( P[i][1] + dp(i+1,1), dp(i+1,0) )
                else:
                    pay = max( P[i][0] + dp(i+1,1), dp(i+1,0) )

            return pay

        self.setSolution(dp(0,0))
            

        
