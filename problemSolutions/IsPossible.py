from Solution import Solution

class IsPossible(Solution):
    '''
    Consider a pair of integers, (a, b). The following operations can be performed on (a, b) in any 
    order, zero or more times.

        (a, b) -> (a + b, b)
        (a, b) -> (a, a + b)

    Return a string that denotes whether or not (a, b)can be converted to (c, d) by performing the 
    operation zero or more times.
    '''

    def __init__(self):
        super().__init__()
        
    def solution(self, sx: int, sy: int, tx: int, ty: int) -> None:
        
        # We see if we can reach (sx,sy) by working backwards.

        # If this condition is not met, we cannot move backwards
        while tx >= sx and ty >= sy:

            # No operations can me made to arrive at this case so we break
            if tx == ty:
                break

            # Otherwise we have two cases

            #######################################################
            # Case 1 
            #######################################################
            # x coordinate is larger than the y coordinate
            elif tx > ty:
                # As long as ty > sy:
                #   tx = (k * ty) + oldx
                # i.e. 
                #   oldx = tx % ty
                if ty > sy:
                    tx = tx % ty
                # Otherwise ty is not changing. In order to go from sx
                # to tx (forwards) we must have
                #   sx + k * ty = tx 
                # i.e. 
                #   (tx - sx) % ty = 0
                else:
                    return (tx - sx) % ty == 0

            #######################################################
            # Case 2
            #######################################################
            # y coordinate is larger than the x coordinate
            # [Same arguments as before]
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0

        self.setSolution(tx == sx and ty == sy)