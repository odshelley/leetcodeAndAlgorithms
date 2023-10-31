from Solution import Solution

class WorldSeries(Solution):
    '''
    This class is for solving the following problem taken from 'Heard on the Street':

    They call this the "World Series" problem in the US. Sports teams "A" and "B" are to play each other until 
    one has four wins and is declared the series winner. You have 100 to bet on Team A to win the series. 
    You are, however, only allowed to bet on individual games, not the final outcome directly, and, you must bet 
    a positive amount on each game. So, if Team A wins the series, you must walk away with 200, but if Team 
    A loses the series, you must walk away with zero, and you must do so having placed a non-zero bet on every 
    game. Your best assessment is that Team A has a 70% chance of winning any game and Team $B$ has a 30% chance. 
    How do you place your bets?
    '''

    def __init__(self):
        super().__init__() 

    def solution(self, wins: int, initial: float) -> None:
        '''
        Parameters
        ----------
        wins : Number of wins either team needs to achieve in order to be declared the winner.

        initial: Your initial capital that needs to be doubled if team A wins and lost if 
        team A loses.
            
        Returns
        -------
        updates answer to be a list describing the betting strategy.
        '''

        amount = [[None]*k for k in range(1,wins+1)] + [[None]*k for k in range(wins+1,1,-1)]
        bet    = [[None]*k for k in range(1,wins+1)] + [[None]*k for k in range(wins+1,1,-1)]

        # Base Cases
        for i in range(1,wins+1):
            amount[-i][0] = 2*initial
            amount[-i][-1], bet[-i][0], bet[-i][-1] = 0, 0, 0
        
        # Inductive steps
        for i in range(2*wins-2,wins-1,-1):
            for j in range(len(amount[i])):
                if amount[i][j] == None:
                    amount[i][j] = 0.5*(amount[i+1][j]+amount[i+1][j-1])
                    bet[i][j]    = 0.5*(amount[i+1][j-1]-amount[i+1][j])
        for i in range(wins-1,-1,-1):
            for j in range(len(amount[i])):
                if amount[i][j] == None:
                    amount[i][j] = 0.5*(amount[i+1][j+1]+amount[i+1][j])
                    bet[i][j]    = 0.5*(amount[i+1][j]-amount[i+1][j+1])

        self.setSolution(bet,amount)
            
            