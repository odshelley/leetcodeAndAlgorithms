from Solution import Solution 

class CountPalindromes(Solution):
    '''
    A palindrome is a string that reads the same from the l and from the r. For example, 
    mom and tacocat are palindrome, as are any single-character strings. Given a string, determine 
    the number of its substring that are palindromes.
    '''
    def __init__(self):
        super().__init__() 
    
    def solution(self, s: str) -> None:

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


        