import unittest
import Graph
import magician


class TestClass(unittest.TestCase):

    def testGraph(self):
        """Ensures that the Bellman Ford algorithm works."""

        g = Graph.Graph(5,True)
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

        paths = [[0,1,1],[0,4,1],[1,2,2],[2,3,4],[4,3,7]]

        # Test1
        s1 = magician.Solution()
        n = 5 
        src = 0
        trgt = 3
        spells = 1
        s1.magician(n,src,trgt,spells,paths)
        self.assertEqual(s1.answer, 1, "incorrect distance")

        # Test 2
        s2 = magician.Solution()
        g = Graph.Graph(5,False)
        for x in paths:
            g.addEdge(x[0],x[1],x[2])
        s2.magician(5,0,3,0,paths)
        self.assertEqual(s2.answer, g.bellmanFord(0)[3], "incorrect distance")
       
if __name__ == '__main__':
    unittest.main()