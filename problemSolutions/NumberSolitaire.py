from Solution import Solution 

class NumberSolitaire(Solution):
    '''
    This class is for solving the following problem taken from Codility:

    A game for one player is played on a board consisting of N consecutive squares, numbered from 0 to N − 1. 
    There is a number written on each square. A non-empty array A of N integers contains the numbers written on 
    the squares. Moreover, some squares can be marked during the game.

    At the beginning of the game, there is a pebble on square number 0 and this is the only square on the board 
    which is marked. The goal of the game is to move the pebble to square number N − 1.

    During each turn we throw a six-sided die, with numbers from 1 to 6 on its faces, and consider the number K, 
    which shows on the upper face after the die comes to rest. Then we move the pebble standing on square number 
    I to square number I + K, providing that square number I + K exists. If square number I + K does not exist, 
    we throw the die again until we obtain a valid move. Finally, we mark square number I + K.

    After the game finishes (when the pebble is standing on square number N − 1), we calculate the result. The 
    result of the game is the sum of the numbers written on all marked squares.
    '''

    def __init__(self):
        super().__init__()
    
    def solution(self, A: list[int]) -> None:
        '''
        Parameters
        ----------
        A : list of costs on board
            
        Returns
        -------
        updates answer to maximum sum you can achieve
        '''
        N = len(A)
        dp = [0]*N
        dp[0] = A[0]

        for i in range(1,N):
            maximum = -float('inf')
            for die_roll in range(1,7):
                if i - die_roll >=0:
                    maximum = max( maximum, dp[i-die_roll] + A[i] )
            dp[i] = maximum 

        self.setSolution(dp[N-1])
