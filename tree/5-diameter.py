#Diameter of a binary Tree
# Three ways
# 1. diameter of left Tree
# 2. diameter of right Tree
# 3. height of left tree + height of right tree + 1


class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    
    def insert(self,data):
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
    
    def diameter(self, root):
        if root is None:
            return 0
        left  = self.diameter(root.left)
        right = self.diameter(root.right)
        both = self.height(root.left) + self.height(root.right) + 1
        return max(left, max(right,both))

    def diameterFast(self, root):
        pass
    
    def height(self,root):
        if root is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        ans = max(left, right) + 1
        return ans

root = Tree(10)
root.insert(3)
root.insert(30)
root.insert(1)
root.insert(2)
root.insert(20)
root.insert(40)
root.insert(50)

print("Tree elements are: \n")
root.printTree()

print("\n\nHeight of tree is: \n")
height = root.height(root)
print(height)

print("\n\nDiameter of a tree is: \n")
result = root.diameter(root)
print(result)

