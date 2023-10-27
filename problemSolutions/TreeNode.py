
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def bfs(self) -> list[any]:

        levels = []

        def helper(node, level: int):
            if len(levels) == level:
                levels.append([]) 
            if node == None:
                levels[level].append('null')
            else:
                levels[level].append(node.val)
                helper(node.left,level+1)
                helper(node.right,level+1)
        
        helper(self,0)
        return levels
    
    def equal(self, A) -> bool:
        return self.bfs() == A.bfs()
