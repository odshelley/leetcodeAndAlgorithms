from Solution import Solution
from TreeNode import TreeNode

class ConstructBinaryTreeFromInorderAndPostorderTraversal(Solution):
    '''
    This class is for solving the following problem:

    Given two integer arrays inorder and postorder where inorder is the inorder traversal of a 
    binary tree and postorder is the postorder traversal of the same tree, construct and return 
    the binary tree.
    '''

    def __init__(self):
        super().__init__()

    def solution(self, inorder: list[int], postorder: list[int]) -> None:
        '''
        Parameters
        ----------
        inorder : list of nodes in inorder sequence

        postorder : list of nodes in postorder sequence
            
        Returns
        -------
        updates answer to be the binary tree
        '''
        def helper(in_left, in_right):
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None
            
            # pick up the last element as a root
            val = postorder.pop()
            root = TreeNode(val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[val]
 
            # build right subtree
            root.right = helper(index + 1, in_right)
            # build left subtree
            root.left = helper(in_left, index - 1)
            return root
        
        idx_map = {val:idx for idx, val in enumerate(inorder)} 

        self.setSolution(helper(0, len(inorder) - 1))