from Solution import Solution

class RobotBoundedInCircle(Solution):
    '''
    Build a computer simulation of a mobile robot. The robot moves on an infinite plane, starting 
    from position (0, 0). Its movements are described by a command string consisting of one or more 
    of the following three letters:

        G  instructs the robot to move forward one step.
        L  instructs the robot to turn left in place.
        R  instructs the robot to turn right in place.

    The robot performs the instructions in a command sequence in an infinite loop. Determine 
    whether there exists some circle such that the robot always moves within the circle.
    '''

    def __init__(self):
        super().__init__()

    def solution(self, commands: list[str]) -> None:

        
        def loop(command):

            directions = ['u','r','d','l']
            directionIdx = 0
            position = [0,0]

            for c in command:
                if c == 'G':
                    if directions[directionIdx] == 'u':
                        position[0] += 1
                    elif directions[directionIdx] == 'd':
                        position[0] -= 1
                    elif directions[directionIdx] == 'r':
                        position[1] += 1
                    else:
                        position[1] -= 1
                elif c == 'R':
                    directionIdx = (directionIdx + 1)%4
                else:
                    directionIdx = (directionIdx - 1)%4

            if (directions[directionIdx] != 'u') or (position == [0,0]):
                return True
            else:
                return False
        
        returnArray = []
        for command in commands:
            returnArray.append(loop(command))

        self.setSolution(returnArray)