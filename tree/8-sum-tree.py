#Sum Tree


class Tree:
    def __init__(self, data):
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

    #this is postorder approach (LRN)
    def isSumTree(self, root):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return root.data

        left = self.isSumTree(root.left)
        right = self.isSumTree(root.right)
        if left + right != root.data:
            return False
        return left+right+root.data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, end=" ")
        if self.right:
            self.right.printTree() 

root = Tree(22)
root.left = Tree(10)
root.right = Tree(2)
root.left.left = Tree(5)
root.left.right = Tree(5)

print("Printing The Tree: \n")
root.printTree()
result = root.isSumTree(root)
if result:
    print("\nThis is Sum Tree")
else:
    print("\nThis is not a sum tree.")