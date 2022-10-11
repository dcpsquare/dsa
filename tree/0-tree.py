class Tree:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
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

root = Tree(10)
root.insert(11)
root.insert(12)
root.insert(13)
root.insert(14)
root.insert(15)
root.insert(16)

print("Tree Elements are: ")
root.printTree()