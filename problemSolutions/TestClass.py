import unittest
from Graph import Graph
from Magician import Magician
from Salary import Salary
from BestTimeToBuyAndSellStock import BestTimeToBuyAndSellStock


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
        s1.solution2(n,src,trgt,spells,paths1)
        self.assertEqual(s1.getSolution(), 1, "incorrect distance")

        # Test 2
        s2 = Magician()
        g = Graph(5,False)
        for x in paths1:
            g.addEdge(x[0],x[1],x[2])
        s2.solution(5,0,3,0,paths1)
        self.assertEqual(s2.getSolution(), g.bellmanFord(0)[3], "incorrect distance")
        s2.solution2(5,0,3,0,paths1)
        self.assertEqual(s2.getSolution(), g.bellmanFord(0)[3], "incorrect distance")

        # Test3
        s3 = Magician()
        n, src, trgt, spells = 4, 2, 1, 1
        s3.solution(n,src,trgt,spells,paths2)
        self.assertEqual(s3.getSolution(), 2, "incorrect distance")
        s3.solution2(n,src,trgt,spells,paths2)
        self.assertEqual(s3.getSolution(), 2, "incorrect distance")
       
    def testSalary(self):
        """Ensures that the Magician solution is correct."""

        # Test1
        s1 = Salary()
        n, m = 4, 2 
        p = [[1,2],[4,10],[20,21],[2,23]]
        s1.solution(n,m,p)
        self.assertEqual(s1.getSolution(), 33, "incorrect amount")

        # Test2
        s2 = Salary()
        n, m = 3, 2 
        p = [[1,2],[4,100],[1,1000]]
        s2.solution(n,m,p)
        self.assertEqual(s2.getSolution(), 1002, "incorrect amount")

    def testBestTimeToBuyAndSellStock(self):
        """Ensures that the testBestTimeToBuyAndSellStock solutions are correct."""

        # Test1
        s1 = BestTimeToBuyAndSellStock()
        k, prices = 2, [2,4,1] 
        s1.solution(k,prices)
        self.assertEqual(s1.getSolution(), 2, "incorrect answer")

        # Test2
        s2 = BestTimeToBuyAndSellStock()
        k, prices = 2, [3,2,6,5,0,3]
        s2.solution(k,prices)
        self.assertEqual(s2.getSolution(), 7, "incorrect answer")

        # Test3
        s3 = BestTimeToBuyAndSellStock()
        prices = [3,3,5,0,0,3,1,4]
        s3.solution3(prices)
        self.assertEqual(s3.getSolution(), 6, "incorrect answer")

if __name__ == '__main__':
    unittest.main()