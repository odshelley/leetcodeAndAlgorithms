from Solution import Solution

class PlusMultArray(Solution):
    '''
    A is an array of integers described as {A[0], A[1], A[2], A[3], ...,A[n-1]}. Perform the 
    following calculations on the elements of A:

        $R_{\text {even }}=(((((A[0] x A[2])+A[4]) * A[6])+A[8]) * \ldots)$
        $\left.R_{\text {odd }}=((((A[1] x A[3])+A[5]) * A[7])+A[9]) * \ldots\right)$

    You can then use R_even and R_odd to determine if A is odd, even, or neutral using the 
    criterion below:
        * If R_odd > R_even , then A is ODD
        * If R_even > R_odd, then A is EVEN.
        * If R_odd = R_even, then A is NEUTRAL
    '''

    def __init__(self):
        super().__init__()

    def solution(self, A: list[int]) -> None:

        Reven = A[0]
        Rodd  = A[1]
        for i in range(1,int(len(A)//2)):
            if i%2 == 1:
                Reven *= A[2*i]
                Rodd  *= A[2*i+1]
            else:
                Reven += A[2*i]
                Rodd  += A[2*i+1]

        Reven = Reven % 2
        Rodd  = Rodd % 2

        if Reven > Rodd:
            self.setSolution('EVEN')
            return
        elif Rodd > Reven:
            self.setSolution('ODD')
            return
        else:
            self.setSolution('NEUTRAL')
            return