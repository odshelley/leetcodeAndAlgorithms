import unittest
from Graph import Graph
from TreeNode import TreeNode
from Magician import Magician
from Salary import Salary
from BestTimeToBuyAndSellStock import BestTimeToBuyAndSellStock
from BestTimeToBuyAndSellStockWithCooldown import BestTimeToBuyAndSellStockWithCooldown
from NumberSolitaire import NumberSolitaire
from ConstructBinaryTreeFromInorderAndPostorderTraversal import ConstructBinaryTreeFromInorderAndPostorderTraversal
from PaintFence import PaintFence
from WorldSeries import WorldSeries
from isSubsequence import isSubsequence
from Triangle import Triangle
from UnionFind import UnionFind
from TheEarliestMomentWhenEveryoneBecomeFriends import TheEarliestMomentWhenEveryoneBecomeFriends


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

    def testBestTimeToBuyAndSellStockWithCooldown(self):
        """Ensures that the testBestTimeToBuyAndSellStockWithCooldown solutions are correct."""
        # Test 1
        s1 = BestTimeToBuyAndSellStockWithCooldown()
        prices = [1,2,3,0,2]
        s1.solution(prices)
        self.assertEqual(s1.getSolution(), 3, "incorrect answer")

    def testNumberSolitaire(self):
        
        """Ensures that the NumberSolitaire solution is correct."""
        # Test 1
        s1 = NumberSolitaire()
        A = [1,-2,0,9,-1,-2]
        s1.solution(A)
        self.assertEqual(s1.getSolution(), 8, "incorrect answer")

    def testConstructBinaryTreeFromInorderAndPostorderTraversal(self):
         """Ensures that the ConstructBinaryTreeFromInorderAndPostorderTraversal solution is correct."""
         s1 = ConstructBinaryTreeFromInorderAndPostorderTraversal()
         A = [9,3,15,20,7]
         B = [9,15,7,20,3]
         s1.solution(A,B)
         leaf1 = TreeNode(9)
         leaf2 = TreeNode(20,TreeNode(15),TreeNode(7))
         tree1 = TreeNode(3,leaf1,leaf2)
         self.assertTrue( s1.getSolution().equal(tree1), "incorrect answer")
    
    def testPaintFence(self):

        # Test1
        s1 = PaintFence()
        n, k = 1, 1 
        s1.solution(n,k)
        self.assertEqual( s1.getSolution(), 1, "incorrect answer" )

        # Test1
        s2 = PaintFence()
        n, k = 7, 2
        s2.solution(n,k)
        self.assertEqual( s2.getSolution(), 42, "incorrect answer" )

    def testWorldSeries(self):
        return None

    def testIsSubsequence(self):
        
        # Test1
        s1 = isSubsequence()
        s = 'abc'
        t = 'ahbgdc'
        s1.solution(s,t)
        self.assertEqual( s1.getSolution(), True, "incorrect answer" )

    def testTriangle(self):
        # Test1
        s1 = Triangle()
        triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
        s1.solution(triangle)
        self.assertEqual( s1.getSolution(), 11, "incorrect answer" )

    def testUnionFind(self):
        # Test1
        uf = UnionFind(10)
        # 1-2-5-6-7 3-8-9 4
        uf.union(1, 2)
        uf.union(2, 5)
        uf.union(5, 6)
        uf.union(6, 7)
        uf.union(3, 8)
        uf.union(8, 9)
        self.assertTrue(uf.connected(1, 5))
        self.assertTrue(uf.connected(5, 7))
        self.assertFalse(uf.connected(4, 9))

    def testTheEarliestMomentWhenEveryoneBecomeFriends(self):
        # Test1
        s1 = TheEarliestMomentWhenEveryoneBecomeFriends()
        logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
        n = 6
        s1.solution(logs,n)
        self.assertEqual( s1.getSolution(), 20190301, "incorrect answer" )


if __name__ == '__main__':
    unittest.main()