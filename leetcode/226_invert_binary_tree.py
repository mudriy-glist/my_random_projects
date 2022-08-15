# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if node:                                          # node is not null
                node.left, node.right = node.right, node.left # swap left & right
                dfs(node.left)                                # repeat for left
                dfs(node.right)                               # repeat for right
        dfs(root)                                             # start with root
        return root