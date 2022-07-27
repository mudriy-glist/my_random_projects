from itertools import izip
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse(node):
    if not node:
        yield None
    else:
        yield node.val
        for val in traverse(node.left):
            yield val
        for val in traverse(node.right):
            yield val
            
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        try:
            for node_p, node_q in izip(traverse(p), traverse(q)):
                if node_p != node_q:
                    return False
        except StopIteration:
            return True

        return True