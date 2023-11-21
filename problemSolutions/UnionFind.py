class UnionFind:
    """
    A class for performing union find on a graph

    ...

    Attributes
    ----------
    root : List[int]
        root of each node
    rank : List[int]
        stating if the graph is undirected or not
    count : int
        number of connected components

    Methods
    -------
    find(x):
    union(x,y):
    getCount()
    connected(x, y)
    """
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1

    def getCount(self):
        return self.count

    def connected(self, x, y):
        return self.find(x) == self.find(y)