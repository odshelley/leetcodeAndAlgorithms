from Solution import Solution

class ChairsSurplus(Solution):
    '''
    In this challenge, determine the minimum number of chairs to be purchased to accommodate all 
    workers in a new business workroom. There is no chair at the beginning.

    There will be a string array of simulations. Each simulation is described by a combination of 
    four characters: C, R, U, and L
        * C - A new employee arrives in the workroom. If there is a chair available, the employee 
        takes it. Otherwise, a new one is purchased.
        * R - An employee goes to a meeting room, freeing up a chair.
        * U - An employee arrives from a meeting room. If there is a chair available, the employee 
          takes it. Otherwise, a new one is purchased.
        * L - An employee leaves the workroom, freeing up a chair.
    '''

    def __init__(self):
        super().__init__()

    def solution(self, simulations: list[str]) -> None:

        def chairsRequired(sim):
            availableChairs = 0
            purchased = 0

            for situation in sim:
                if situation == 'C' or situation == 'U':
                    if availableChairs == 0:
                        purchased += 1
                    else:
                        availableChairs -= 1
                if situation == 'R' or situation == 'L':
                    availableChairs = availableChairs + 1
      
            return purchased
        
        resultArray = []
        for simulation in simulations:
            resultArray.append(chairsRequired(simulation))

        self.setSolution(resultArray)