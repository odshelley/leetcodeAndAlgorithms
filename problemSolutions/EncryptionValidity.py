from Solution import Solution 

class EncryptionValidity(Solution):
    '''
    Given the number of keys, a hijacker can test per second, determine if the encrypted 
    information should remain confidential throughout its validity period. Each test will 
    return two items of information as integers:

        - Can a hijacker crack the code within the period? (1 if true, 0 if false)
        - The strength of the encryption, that is, the number of keys that must be tested 
          to break the encryption.
    
    The strength of the encryption is determined as follows:

        - Keys is a list of positive integers, keys[i], that act as keys.
        - The degree of divisibility of an element is the number of elements in the set 
          keys that are greater than 1 and are divisors of the element, i.e element modulo 
          divisor = 0
        - The element m that has the maximum number of divisors (or degree of divisibility) 
          in keys is used to determine the strength of the encryption.
        - The strength of the encryption is defined as 
          (the degree of divisibility of m) * 10^5
    '''
    def __init__(self):
        super().__init__() 
    
    def solution(self, instructionCount: int, validityPeriod: int, keys: list[int]) -> None:

        frequency = {}
        maximum = 0
    
        for i in keys:
            frequency[i] = frequency.get(i, 0) + 1
    
        for idx in range(len(keys)):

            num = keys[idx]
            count = 0
    
            # Iterate through each possible divisor of num
            for j in range(1, int(math.sqrt(num)) + 1):
                # If j is a divisor of num and present in 'keys', count it
                if (num % j == 0):
                    if j in frequency:
                        count += frequency[j]
    
                    # If j is not equal to num/j and present in 'keys',
                    # count num/j as well as divisors exist in pairs
                    if j != num // j and num // j in frequency:
                        count += frequency[num // j]
    
            maximum = max(count, maximum)
    
        hackerTime = instructionCount * validityPeriod
    
        if hackerTime >= maximum * 100000:
            self.setSolution([1, maximum * 100000])
        else:
            self.setSolution([0, maximum * 100000])
    