from Solution import Solution 

class ThresholdAlerts(Solution):
    '''
    A compliance system monitors incoming and outbound calls. It sends an alert whenever 
    the average number of calls over a trailing number of minutes exceeds a threshold. If 
    the number of trailing minutes to consider, precedingMinutes = 5, at time T, take the 
    average the call volumes for times T-(5-1), T-(5-2) ... T-(5-5).
    '''
        
    def __init__(self):
        super().__init__() 
    
    def solution(self, precedingMinutes: int, alertThreshold: int, numCalls: list[int]) -> None:

        count = 0
        avg = 0

        for i in range(precedingMinutes):
            avg += numCalls[i]/precedingMinutes
        if avg > alertThreshold:
            count += 1 
        
        start = 0
        end = precedingMinutes

        while end < len(numCalls):

            avg = avg + (numCalls[end]-numCalls[start])/precedingMinutes
            if avg > alertThreshold:
                count += 1 
                
            start += 1
            end += 1
            
        self.setSolution(count)

        