from Solution import Solution

class isSubsequence(Solution):
    '''
    This class is for solving the following problem taken from Leetcode:

    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original string by deleting 
    some (can be none) of the characters without disturbing the relative positions of the remaining 
    characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not). 
    '''

    def __init__(self):
        super().__init__() 

    def solution(self, s: str, t: str) ->  None:
        '''
        Parameters
        ----------
        s : Possible substring

        t : The string in question
            
        Returns
        -------
        updates answer to be a boolean indicating if s is a substring of t.
        '''
        
        T = len(t)
        S = len(s)
        pt = 0
        ps = 0

        while pt < T and ps < S:
            if s[ps] == t[pt]:
                ps += 1
                pt += 1
            else:
                pt += 1
        self.setSolution(ps == S)