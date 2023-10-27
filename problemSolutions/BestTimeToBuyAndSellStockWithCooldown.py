from Solution import Solution
import functools

class BestTimeToBuyAndSellStockWithCooldown(Solution):
    '''
    This class is for solving the following problem:

    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., 
    buy one and sell one share of the stock multiple times) with the following restrictions:

    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock 
    before you buy again).
    '''

    def __init__(self):
        super().__init__()

    def solution(self, prices: list[int]) -> None:
        '''
        Parameters
        ----------
        prices : list of prices of a given stock 
            
        Returns
        -------
        updates answer to maximum profit you can achieve
        '''
        N = len(prices)
        @functools.lru_cache
        def dp(day,cooldown,holding):
            if day == N:
                return 0
            
            if cooldown == 1:
                return dp(day+1,0,0)
            else:
                do_nothing = dp(day+1,0,holding)
                do_something = 0 
                
                if holding == 1:
                    do_something =  prices[day] + dp(day+1,1,0)
                else:
                    do_something = -prices[day] + dp(day+1,0,1)
                    
            return max(do_something, do_nothing)
        
        self.setSolution(dp(0,0,0))
            
        

    