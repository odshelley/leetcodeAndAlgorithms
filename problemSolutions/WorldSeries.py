from Solution import Solution

class WorldSeries(Solution):

    def __init__(self):
        super().__init__() 

    def solution(self, wins: int, initial: float) -> None:

        dp   = [[None]*k for k in range(1,wins+1)] + [[None]*k for k in range(wins+1,1,-1)]
        bets = [[None]*k for k in range(1,wins+1)] + [[None]*k for k in range(wins+1,1,-1)]

        # Base Cases
        for i in range(1,wins+1):
            dp[-i][0]    = 2*initial
            dp[-i][-1],bets[-i][0],bets[-i][-1] = 0, 0, 0
        
        # Inductive steps
        for i in range(2*wins-2,wins-1,-1):
            for j in range(len(dp[i])):
                if dp[i][j] == None:
                    dp[i][j]   = 0.5*(dp[i+1][j]+dp[i+1][j-1])
                    bets[i][j] = 0.5*(dp[i+1][j-1]-dp[i+1][j])
        for i in range(wins-1,-1,-1):
            for j in range(len(dp[i])):
                if dp[i][j] == None:
                    dp[i][j]   = 0.5*(dp[i+1][j+1]+dp[i+1][j])
                    bets[i][j] = 0.5*(dp[i+1][j]-dp[i+1][j+1])

        self.setSolution(bets,dp)
            
            