# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def MaximumDepth(self, root):
            if root is None:
                return 0
            return max(self.MaximumDepth(root.left), self.MaximumDepth(root.right)) + 1
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root == None:
            return True

        left_height = self.MaximumDepth(root.left)
        right_height = self.MaximumDepth(root.right)

        if (abs(left_height - right_height) <= 1) and self.isBalanced(
        root.left) is True and self.isBalanced(root.right) is True:
            return True

        return False