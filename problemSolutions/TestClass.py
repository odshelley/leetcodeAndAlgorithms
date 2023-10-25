import unittest
from Graph import Graph
from Magician import Magician

class TestClass(unittest.TestCase):

    def testGraph(self):
        """Ensures that the Bellman Ford algorithm works."""

        g = Graph(5,True)
        g.addEdge(1,0,1)
        g.addEdge(2,0,3)
        g.addEdge(1,2,2)
        g.addEdge(2,1,1)
        g.addEdge(3,1,8)
        g.addEdge(4,2,2)
        g.addEdge(3,4,4)
        g.addEdge(4,3,2)

        self.assertEqual(g.bellmanFord(0), [0, 1, 2, 8, 4], "incorrect distances")

    def testMagician(self):
        """Ensures that the Magician solution is correct."""

        paths1 = [[0,1,1],[0,4,1],[1,2,2],[2,3,4],[4,3,7]]
        paths2 = [[0,1,2],[0,2,10],[1,3,5],[2,3,5]]

        # Test1
        s1 = Magician()
        n, src, trgt, spells = 5, 0, 3, 1
        s1.solution(n,src,trgt,spells,paths1)
        self.assertEqual(s1.getSolution(), 1, "incorrect distance")

        # Test 2
        s2 = Magician()
        g = Graph(5,False)
        for x in paths1:
            g.addEdge(x[0],x[1],x[2])
        s2.solution(5,0,3,0,paths1)
        self.assertEqual(s2.getSolution(), g.bellmanFord(0)[3], "incorrect distance")

        # Test3
        s3 = Magician()
        n, src, trgt, spells = 4, 2, 1, 1
        s3.solution(n,src,trgt,spells,paths2)
        self.assertEqual(s3.getSolution(), 2, "incorrect distance")
       
if __name__ == '__main__':
    unittest.main()