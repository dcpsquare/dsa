# Binary Tree Right View
# Sol : print first node of every level from right

class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.level = 0
        self.values = {}
        self.result = []


    def rightViewTraversal(self, root, level, values):
        if root is None:
            return
        
        if level in values:
            pass
        else:
            values[level] = root.data

        self.rightViewTraversal(root.right, level + 1, values)
        self.rightViewTraversal(root.left, level + 1, values)

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.right = Tree(5)
root.right.right = Tree(4)

print("printing right view of tree: \n")
root.rightViewTraversal(root, root.level, root.values)
for x in root.values.keys():
    root.result.append(root.values[x])

print(root.result)