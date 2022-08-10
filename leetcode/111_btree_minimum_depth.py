# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        min_depth = min(left, right) + 1
        max_depth = max(left, right) + 1
        if min_depth == 1:
            return max_depth
        
        return min_depth