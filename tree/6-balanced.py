# check if binary tree is balanced


class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root):
        if root is None:
            return True
        left  = self.isBalanced(root.left)
        right  = self.isBalanced(root.right)
        ans =  abs(self.height(root.left)- self.height(root.right)) <= 1
        if left and right and ans:
            return True
        else:
            return False


root = Tree(10)
root.insert(3)
root.insert(30)
root.insert(1)
root.insert(20)

res = root.isBalanced(root)
print(res)