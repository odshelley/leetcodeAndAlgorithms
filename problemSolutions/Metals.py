from Solution import Solution

class Metals(Solution):
    '''
    The owner of a construction company has a surplus of rods of arbitrary lengths. A local 
    contractor offers to buy any of the surplus, as long as all the rods have the same 
    exact integer length, referred to as saleLength. The number of sellable rods can be 
    increased by cutting each rod zero or more times, but each cut has a cost denoted by 
    costPerCut. After all cuts have been made, any leftover rods having a length other than 
    saleLength must be discarded for no profit. The owner's total profit for the sale is 
    calculated as:

        totalProfit = totalUniFormRods * saleLength * salePrice - totalCuts * costPerCut
    
    where totalUniformRods is the number of sellable rods, salePrice is the per unit length 
    price that the contractor agrees to pay, and the totalCuts is the total number of times 
    the rods needed to be cut.
    '''

    def __init__(self):
        super().__init__()

    def solution(costPerCut,salePrice,lengths):

        maxProfit = 0

        for sale_length in range(1,max(lengths)):
            
            profit = 0

            for rod in lengths:
                numberAfterCuts = rod // sale_length
                if rod % sale_length == 0:
                    gain = max(numberAfterCuts * salePrice * sale_length - (numberAfterCuts - 1) * costPerCut, 0)
                elif  numberAfterCuts > 0:
                    gain = max(numberAfterCuts * (salePrice * sale_length - costPerCut), 0)
                else:
                    gain = 0

                profit += gain 

            oldProfit = maxProfit
            maxProfit = max(profit, maxProfit)

            if maxProfit < oldProfit:
                break

        self.setSolution(maxProfit)
            

