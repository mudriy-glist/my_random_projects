# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSymmetricHelper(root.left, root.right)

    def isSymmetricHelper(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False 
        out = True
        out = out and self.isSymmetricHelper(node1.left, node2.right)
        if not out:
            return False
        out = out and self.isSymmetricHelper(node1.right, node2.left)
        return out