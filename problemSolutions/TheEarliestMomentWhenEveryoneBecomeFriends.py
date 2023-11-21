from UnionFind import UnionFind
from Solution import Solution 


class TheEarliestMomentWhenEveryoneBecomeFriends(Solution):
    '''
    There are n people in a social group labeled from 0 to n - 1. You are given an array 
    logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at 
    the time timestampi.

    Friendship is symmetric. That means if a is friends with b, then b is friends with a. 
    Also, person a is acquainted with a person b if a is friends with b, or a is a friend 
    of someone acquainted with b.

    Return the earliest time for which every person became acquainted with every other 
    person. If there is no such earliest time, return -1.
    '''

    def __init__(self):
        super().__init__()
    
    def solution(self, logs: list[list[int]], n: int) -> None:
        '''
        Parameters
        ----------
        logs : the time two people meet
        n    : the number of people
            
        Returns
        -------
        updates answer to the first time everyone is acquainted
        '''

        logs = sorted(logs, key=lambda x: x[0])
        uf = UnionFind(n)
        
        for log in logs:
            uf.union(log[1],log[2])
            if uf.count == 1:
                self.setSolution(log[0])
                return

        self.setSolution(-1)

