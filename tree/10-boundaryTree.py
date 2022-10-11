# Boundary Travarsal


class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.result = []

    def traverseLeft(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        if root.left is not None:
            self.result.append(root.data)
            self.traverseLeft(root.left)
        else:
            self.traverseRight(root)

    def traverseRight(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return

        if root.right:
            self.traverseRight(root.right)
            self.result.append(root.data)
        else:
            self.traverseLeft(root)

    def traverseLeaf(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.result.append(root.data)
        self.traverseLeaf(root.left)
        self.traverseLeaf(root.right)

    def boundaryTraversal(self,root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        self.result.append(root.data)

        self.traverseLeft(root.left)
        self.traverseLeaf(root)
        self.traverseRight(root.right)

root = Tree(1)
root.left = Tree(2)
root.right = Tree(4)
root.left.left = Tree(3)
root.left.right = Tree(5)
root.left.right.left = Tree(6)
root.left.right.right = Tree(8)
root.right.right = Tree(7)
root.right.right.right = Tree(9)
root.right.right.right.left = Tree(10)
root.right.right.right.right = Tree(11)

print("Printing elements in boundry traversal: \n")
root.boundaryTraversal(root)
print(root.result)
