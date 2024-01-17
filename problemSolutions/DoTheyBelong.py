from Solution import Solution

class DoTheyBelong(Solution):
    '''
    A triangle formed by the three points a(x1, y1), b (x2, y2) and c(x3, y3) is a 
    non-degenerate triangle if the following rules are respected (|ab| is the length of the 
    line between points a and b):

        |ab| + |bc| > |ac|
        |bc| + |ac| > |ab|
        |ab| + |ac| > |bc|
    
    A point belongs to a triangle if it lies somewhere on or inside the triangle. Given two 
    points p = (xp, yp) and q = (xq, yq), return the correct scenario number: 
    
        0: If the triangle abc does not from a valid non-degenerate triangle.
        1: If point p belongs to the triangle but point q does not.
        2: If point q belongs to the triangle but point p does not.
        3: If both points p and q belong to the triangle.
        4: If neither point p nor point q belong to the triangle.

    '''

    def __init__(self):
        super().__init__()

    def solution(self, x1, y1, x2, y2, x3, y3, xp, yp, xq, yq) -> None:

        skip = False
    
        def degenerate(a1,b1,a2,b2,a3,b3):

            ab = abs( (a1-a2)**2 + (b1-b2)**2 )**(.5)
            ac = abs( (a1-a3)**2 + (b1-b3)**2 )**(.5)
            bc = abs( (a2-a3)**2 + (b2-b3)**2 )**(.5)

            if (ab + bc <= ac) or (ab + ac <= bc) or (ac + bc <= ab):
                return True
        
        if degenerate(x1,y1,x2,y2,x3,y3):
            self.setSolution(0)
            skip = True
        
        def area(a1, b1, a2, b2, a3, b3):
            return abs((a1 * (b2 - b3) + a2 * (b3 - b1) + a3 * (b1 - b2)) / 2.0)
        
        
        def isInside(a1, b1, a2, b2, a3, b3, x, y):
        
            # Calculate area of triangle ABC
            A = area (a1, b1, a2, b2, a3, b3)
        
            # Calculate area of triangle PBC 
            A1 = area (x, y, a2, b2, a3, b3)
            
            # Calculate area of triangle PAC 
            A2 = area (a1, b1, x, y, a3, b3)
            
            # Calculate area of triangle PAB 
            A3 = area (a1, b1, a2, b2, x, y)
            
            # Check if sum of A1, A2 and A3 
            # is same as A
            if(A == A1 + A2 + A3):
                return True
            else:
                return False
        
        pInside = isInside(x1, y1, x2, y2, x3, y3, xp, yp)
        qInside = isInside(x1, y1, x2, y2, x3, y3, xq, yq)

        if skip == False:
            if pInside and qInside:
                self.setSolution(3)
            elif pInside:
                self.setSolution(1)
            elif qInside:
                self.setSolution(2)
            else:
                self.setSolution(4)