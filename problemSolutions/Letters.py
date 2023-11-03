from Solution import Solution

class Letters(Solution):

    def __init__(self):
        super.__init__()


    def solution(letters):

        N = len(letters)
        p1 = 0
        total = 0

        while p1 < len(letters):

            if letters[p1].isupper():
                # current position of upper case letter
                currentUpper = p1 
                # move p1 to the next lower case letter or the end of letters
                while p1 < N and letters[p1].isupper():
                    p1 += 1
                # the length of the substring of uppercase letters
                amount = p1 - currentUpper 

                count = 0
                p2 = currentUpper

                for idx in range(max(0,currentUpper-amount),currentUpper):
                    # if the letter 'amount' steps behind letter[p2] is letter[p2].lower()
                    # we update the counter and move p2 to the next position
                    if letters[idx] == letters[p2].lower():
                        count += 1
                        p2 += 1
                    # if the letter 'amount' steps behind letter[p2] is not letter[p2].lower()
                    # we set the counter back to zero and move p2 back to position currentUpper
                    else:
                        p2 = currentUpper
                        count = 0
                # We update the total 
                total += count

            p1 += 1

        self.setSolution(total)