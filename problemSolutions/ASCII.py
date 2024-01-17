from Solution import Solution

class ASCII(Solution):
    '''
    Many simple encoding methods have been devised over the years. A common method is the 
    ASCII character set used to display characters on the screen. Each character is given a 
    numeric value which can be interpreted by the computer.

    To decode the string, first reverse the string of digits, then successively pick valid 
    values from the string and convert them to their ASCII equivalents. Some of the values 
    will have two digits, and others three. Use the ranges of valid values when decoding 
    the string of digits.

    Given a string, decode it following the steps mentioned above.
    '''
    def __init__(self):
        super().__init__()

    def solution(self, encode: str):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        hashMap = { alphabet[i]:97+i for i in range(len(alphabet)) }
        for i,x in enumerate(alphabet):
            hashMap[x.capitalize()] = 65 + i 
        hashMap[' '] = 32

        decode = ''
        for x in encode:
            decode += str(hashMap[x])

        self.setSolution(decode[::-1])

