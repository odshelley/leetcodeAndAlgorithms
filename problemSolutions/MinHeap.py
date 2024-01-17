class MinHeap:
    def __init__(self, heapSize: int):
        self._heapSize = heapSize
        self._minHeap = [0] * (heapSize + 1)
        self._realSize = 0

    def __str__(self):
        return str(self._minHeap[1 : self._realSize + 1])

    def add(self, element: int) -> None:
        self._realSize += 1

        if self._realSize > self._heapSize:
            raise ValueError("Added too many elements!")
        else:
            self._minHeap[self._realSize] = element

            index = self._realSize
            parentIndex = index // 2

            while self._minHeap[index] < self._minHeap[parentIndex] and index > 1:
                self._minHeap[parentIndex], self._minHeap[index] = (
                    self._minHeap[index],
                    self._minHeap[parentIndex],
                )

                index = parentIndex
                parentIndex = index // 2

    def pop(self) -> int:
        if self._realSize < 1:
            raise ValueError("There aren't any elements in the heap!")
        else:
            removeElement = self._minHeap[1]
            self._minHeap[1] = self._minHeap[self._realSize]
            self._realSize -= 1
            index = 1

            while index <= self._realSize // 2:
                leftChild = index * 2
                rightChild = (index * 2) + 1

                if (
                    self._minHeap[index] > self._minHeap[leftChild]
                    or self._minHeap[index] > self._minHeap[rightChild]
                ):
                    if self._minHeap[leftChild] < self._minHeap[rightChild]:
                        self._minHeap[leftChild], self._minHeap[index] = (
                            self._minHeap[index],
                            self._minHeap[leftChild],
                        )
                        index = leftChild
                    else:
                        self._minHeap[rightChild], self._minHeap[index] = (
                            self._minHeap[index],
                            self._minHeap[rightChild],
                        )
                        index = rightChild
                else:
                    break

            return removeElement

    def peek(self) -> int:
        return self._minHeap[1]

    def size(self):
        return self._realSize
