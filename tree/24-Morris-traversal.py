# Morris Traversal without using Stack and recursion

# Tree Traversal
# 1.  InOrder (TC - O(n), SC - O(n))
# 2.  PreOrder (TC - O(n), SC - O(n))
# 3. PostOrder (TC - O(n), SC - O(n))
# 4. LevelOrder (TC - O(n), SC - O(n))
# 5. MorrisTraversal (TC - O(n), SC - O(1))
# In Morris Traversal Space Complexity is O(1)

#   Algorithm
# Note: Here pred (temp link) is used for return 
# from the node as in Inorder, preorder, postorder recursion ex.
''' 
1. Initialize current as root 
2. While current is not NULL
   If the current does not have left child
      a) Print current’s data
      b) Go to the right, i.e., current = current->right
   Else
      a) Find rightmost node in current left subtree OR
              node whose right child == current.
         If we found right child == current
             a) Update the right child as NULL of that node whose right child is current
             b) Print current’s data
             c) Go to the right, i.e. current = current->right
         Else
             a) Make current as the right child of that rightmost 
                node we found; and 
             b) Go to this left child, i.e., current = current->left
'''


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def morrisTraversal(self, root):
        current = root

        while current is not None:
            if current.left is None:
                print(current.data, end=" ")
                # yield current.data
                current = current.right
            
            else:
                # Here we are finding pred
                # below two line will create a temporary link
                # and loop untill pred.right != None and pred.right not start 
                # pointing to the current
                
                pred = current.left
                while pred.right is not None and pred.right is not current:
                    pred = pred.right
                if pred.right is None:
                    pred.right = current
                    current = current.left
                else:
                    pred.right = None
                    # yield current.data
                    print(current.data, end=" ")
                    current = current.right

root = Tree(1)
root.left = Tree(2)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.left.left.right = Tree(7)
root.right = Tree(3)
root.right.right = Tree(6)

root.morrisTraversal(root)