from Solution import Solution 
import heapq


class ProductOfMaxMinDataset(Solution):
    '''
    Starting with an empty set of integers named elements, perform the following query operations:

        * The command push x inserts the value of x into elements.
        * The command pop x removes the value of x from elements.

    The integers in elements need to be ordered in such a way that refer each operation is 
    performed, the product of the maximum and minimum values in the set can be easily calculated.
    '''
        
    def __init__(self):
        super().__init__() 

    class MinMaxSet:
        def __init__(self):
            self.elements = set()
            self.min_heap = []
            self.max_heap = []

        def add(self, value):
            if value not in self.elements:
                self.elements.add(value)
                heapq.heappush(self.min_heap, value)
                heapq.heappush(self.max_heap, -value)

        def remove(self, value):
            if value in self.elements:
                self.elements.remove(value)
                self.min_heap.remove(value)
                heapq.heapify(self.min_heap)

                self.max_heap.remove(-value)
                heapq.heapify(self.max_heap)

        def get_min(self):
            if self.min_heap:
                return self.min_heap[0]
            return None

        def get_max(self):
            if self.max_heap:
                return -self.max_heap[0]
            return None

    def solution(operations: list[str], x: list[int]) -> None:

            elements = MinMaxSet()
            products = []

            for i, operation in enumerate(operations):
                if operation == 'push':
                    elements.add(x[i])
                elif operation == 'pop':
                    elements.remove(x[i])
                    
                products.append(elements.get_min()*elements.get_max())
                
            self.setSolution(products)