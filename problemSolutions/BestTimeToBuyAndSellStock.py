from Solution import Solution
import functools

class BestTimeToBuyAndSellStock(Solution):
    '''
    This class is for solving the 'Best Time To Buy And Sell Stock' problems 
    from Leetcode.

    Best Time To Buy And Sell Stock IV:

    You are given an integer array prices where prices[i] is the price of a 
    given stock on the ith day, and an integer k.

    Find the maximum profit you can achieve. You may complete at most k 
    transactions: i.e. you may buy at most k times and sell at most k times.

    Note: You may not engage in multiple transactions simultaneously (i.e., you 
    must sell the stock before you buy again).
    '''
    def __init__(self):
        super().__init__()

    def solution1(self) -> None:
        return None

    def solution2(self) -> None:
        return None

    def solution3(self, prices: list[int]) -> None:
        '''
        Best Time to Buy and Sell Stock III:

        You are given an array prices where prices[i] is the price of a given 
        stock on the ith day.

        Find the maximum profit you can achieve. You may complete at most two 
        transactions.

        Note: You may not engage in multiple transactions simultaneously (i.e., 
        you must sell the stock before you buy again).


        Parameters
        ----------
        prices : list of prices of a given stock 
            
        Returns
        -------
        updates answer to maximum profit you can achieve
        '''
        self.solution(2, prices)

    def solution(self, k: int, prices: list[int]) -> None:
        '''
        Parameters
        ----------
        k : number of times you can buy and sell

        prices : list of prices of a given stock 
            
        Returns
        -------
        updates answer to maximum profit you can achieve
        '''
        N = len(prices)

        @functools.lru_cache(None)
        def dp(day,transactionsLeft,holding):
            # Base case
            if transactionsLeft == 0 or day == N: 
                return 0 
            
            do_nothing = dp(day+1,transactionsLeft,holding)
            do_something = 0 

            if holding == 1:
                do_something =  prices[day] + dp(day+1, transactionsLeft-1,0)
            if holding == 0:
                do_something = -prices[day] + dp(day+1, transactionsLeft  ,1)
            
            return max(do_nothing, do_something)
        
        self.setSolution(dp(0,k,0))
            
        

    