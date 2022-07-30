

class Node:
    def __init__(self, data=0, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data
    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data <= self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()

    
    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res
    # Preorder traversal
    # Root -> Left ->Right
    def PreorderTraversal(self, root):
      res = []
      if root:
         res.append(root.data)
         res = res + self.PreorderTraversal(root.left)
         res = res + self.PreorderTraversal(root.right)
      return res    
    # Postorder traversal
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res
    def ReturnLeft(self, root):
        res_left = []
        if root:
            res_left = self.ReturnLeft(root.left)
            res_left.append(root.data)
        return res_left
    
    def ReturnRight(self, root):
        res_right = []
        if root:
            res_right = self.ReturnRight(root.right)
            res_right.append(root.data)
        return res_right
    # def MaximumDepth(self, root):
    #     val_l = len(root.ReturnLeft(root))
    #     val_r = len(root.ReturnRight(root))
    #     if val_l > val_r:
    #         return val_l
    #     elif val_r > val_l:
    #         return val_r
    
    def MaximumDepth(self, root):
        if root is None:
            return 0
        return max(self.MaximumDepth(root.left), self.MaximumDepth(root.right)) + 1
    
    def is_balanced(self,root):
        if root is None:
            return 0
        
        left_height = self.MaximumDepth(root.left)
        right_height = self.MaximumDepth(root.right)
        
        if (abs(left_height - right_height) <= 1) and self.is_balanced(root.left) is True and self.is_balanced(root.right) is True:
            return True
        return False
    def MinimumDepth(self, root):
        if root is None:
            return 0
        left = self.MinimumDepth(root.left)
        right = self.MinimumDepth(root.right)
        
        min_depth = min(left, right) + 1
        max_depth = max(left, right) + 1
        if min_depth == 0:
            return max_depth
        
        return min_depth
    
root_list = [2,None,3,None,4,None,5,None,6]
root = Node()
for r in root_list:
    root.insert(r)

var = root.MinimumDepth(root)
print(var)