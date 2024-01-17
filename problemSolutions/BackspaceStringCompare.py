from Solution import Solution 

class BackspaceStringCompare(Solution):
    '''
    Two strings are said to be the same if they are of the same length and have the same 
    character at each index. Backspacing in a string removes the previous character in the 
    string.

    Given two strings containing lowercase English letters and the character # which 
    represents a backspace key, determine if the two final strings are equal. Return 1 if 
    they are equal or 0 if the are not. Note that backspacing an empty string results in an 
    empty string.
    '''
        
    def __init__(self):
        super().__init__() 
    
    def solution(self, s1: str, s2: str) -> None:

        def removeBackspace(string):
            returnArray = []

            for character in string:
                if character != '#':
                    returnArray.append(character)
                elif returnArray:
                    returnArray.pop()
            return "".join(returnArray)
        
        newS1 = removeBackspace(s1)
        newS2 = removeBackspace(s2)

        self.setSolution(int(newS1==newS2))