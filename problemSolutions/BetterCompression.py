from Solution import Solution 

class BetterCompression(Solution):
    '''
    Consider a string, S, that is a series of characters, each followed by its frequency as 
    an integer. The string is not compressed correctly, so there may be multiple occurrences
    of the same character. A properly compressed string will consist of one instance of each
    character in alphabetical order followed by the total count of that character within the
    string.
    '''
        
    def __init__(self):
        super().__init__() 
    
    def solution(self, S: str) -> None:

        compressionMap = {}
        letter = -1
        number = ''
        end = len(S)

        for i in range(end):

            if S[i].isalpha():
                letter = S[i]
                number = ''

            if S[i].isnumeric():
                number += S[i]
                if i + 1 == end:
                    compressionMap[letter] = compressionMap.get(letter,0) + int(number)
                elif S[i+1].isalpha():
                    compressionMap[letter] = compressionMap.get(letter,0) + int(number)

        returnString = ''
        for x in sorted(compressionMap):
            returnString += (x + str(compressionMap[x]))

        self.setSolution(returnString)
        

                
