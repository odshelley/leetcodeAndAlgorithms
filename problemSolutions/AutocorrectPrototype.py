from Solution import Solution

class AutocorrectPrototype(Solution):
    '''
    Complete the implementation of an autocorrect function. Given a search query string, 
    the function should return all words which are anagrams.

    Given 2 arrays, words[n], and queries[q], for each query, return an array of the 
    strings that are anagrams, sorted alphabetically ascending.
    '''

    def __init__(self):
        super().__init__()

    def solution(self, words: list[str], queries: list[str]) -> None:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphaMap = { x:i for i,x in enumerate(alphabet)}

        def anagramTuple(word):
            anagram = [0]*26
            for letter in word:
                anagram[alphaMap[letter]] += 1
            return tuple(anagram)

        anagrams = {}

        for word in words:
            anagram = anagramTuple(word)
            anagrams[anagram] = anagrams.get(anagram,[]) + [word]
       
        returnArray = []

        for query in queries:
            anagram = anagramTuple(query)
            if anagram in anagrams:
                returnArray.append( anagrams[anagram] )

        self.setSolution(returnArray)
