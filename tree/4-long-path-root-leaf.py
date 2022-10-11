#height of a binary Tree 
#Height - longest path between root to leaf

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

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, end=" ")
        if self.right:
            self.right.printTree()
    
    def height(self, root):
        if root is None:
            return 0

        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        return max(leftHeight, rightHeight) + 1

root = Tree(10)
root.insert(3)
root.insert(30)
root.insert(1)
root.insert(2)
root.insert(20)
root.insert(40)
root.insert(50)
root.insert(60)
root.insert(70)

print("Traversing Tree : \n")

root.printTree()

print("\nHeight of a Tree: \n")
height_ = root.height(root)
print(height_)