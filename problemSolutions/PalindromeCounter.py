
from Solution import Solution 
import functools

class PalindromeCounter(Solution):
    '''
    A palindrome is a string that reads the same from the l and from the r. For example, 
    mom and tacocat are palindrome, as are any single-character strings. Given a string, determine 
    the number of its substring that are palindromes.
    '''
        
    def __init__(self):
        super().__init__() 
    
    def solution(self, s: str) -> None:

        # # We take a dynamic programming appraoch
        # n = len(s)
        # dp = [[0] * n for _ in range(n)]

        # # Base Case
        # for i in range(n):
        #     dp[i][i] = 1
            
        # # Recursive Cases
        # for i in range(n - 1, -1, -1):
        #     # We check s[i:j]
        #     for j in range(i + 1, n):
        #         # 
        #         if s[i] == s[j]:
        #             l = i + 1
        #             r = j - 1
        #             while l <= r and s[l] != s[i]:
        #                 l += 1
        #             while l <= r and s[r] != s[i]:
        #                 r -= 1
        #             if l > r:
        #                 dp[i][j] = dp[i + 1][j - 1] * 2 + 2
        #             elif l == r:
        #                 dp[i][j] = dp[i + 1][j - 1] * 2 + 1
        #             else:
        #                 dp[i][j] = dp[i + 1][j - 1] * 2 - dp[l + 1][r - 1]
        #         else:
        #             dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
        # returnAmount = dp[0][n-1]

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        @functools.lru_cache
        def dp(letter, i, j):
            if i > j:
                return 0
            if i == j and s[i] == letter: # Base case
                return 1

            if s[i] == s[j] == letter:
                amount = 2
                for x in alphabet:
                    amount += dp(x, i+1, j-1)
                return amount
            elif s[i] != letter:
                return dp(letter, i+1, j)
            elif s[j] != letter:
                return dp(letter, i, j-1)
        
        n = len(s)
        returnAmount = 0 
        
        for letter in alphabet:
            returnAmount += dp(letter, 0, n-1)

        self.setSolution(returnAmount)


        