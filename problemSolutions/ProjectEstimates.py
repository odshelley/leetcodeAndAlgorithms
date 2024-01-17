from Solution import Solution 

class ProjectEstimates(Solution):
    '''
    A number of bids are being taken for a project. Determine the number of distinct pairs 
    of project costs where their absolute difference is some target value. Two pairs are 
    distinct if they differ in at least one value.
    '''
        
    def __init__(self):
        super().__init__() 
    
    def solution(self, projectCosts: list[int], target:int) -> None:

        
        def binarySearch(arr, low, high, trgt):
            if (high >= low):
                mid = (high + low)//2
                if trgt == arr[mid]:
                    return mid
                elif(trgt > arr[mid]):
                    return binarySearch(arr, (mid + 1), high, trgt)
                else:
                    return binarySearch(arr, low, (mid - 1), trgt)
            return -1
        
        count = 0 
        projectCosts.sort()
        print(projectCosts)

        start = 0
        end = len(projectCosts) -1
        

        while start < end:
            if ( start < end-1 ) and ( projectCosts[start] == projectCosts[start+1] ):
                start += 1
            else:
                flag = binarySearch(projectCosts, start, end, target + projectCosts[start])
                if flag != -1:
                    count += 1
                    start += 1 
                else:
                    start += 1 
                

        self.setSolution(count)