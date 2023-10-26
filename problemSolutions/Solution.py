from abc import ABC, abstractmethod

class Solution(ABC):

    __answer = None # Private 

    def __init__(self,initialise=None):
        self.__answer = initialise

    def setSolution(self,solution) -> None:
        self.__answer = solution

    def getSolution(self):
        return self.__answer
    
    @abstractmethod
    def solution(self) -> None:
        pass