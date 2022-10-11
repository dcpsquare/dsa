# Left View Traversal of Binary Tree

# Sol : print first node of every level from left

class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.h_dist = 0
        self.level = 0
        self.values = {}
        self.result = []

    def leftViewTraversal(self, root, h_dist, level, values):
        if root is None:
            return
        
        if level in values:
            pass
        else:
            values[level] = root.data
        self.leftViewTraversal(root.left, h_dist - 1, level + 1, values)
        self.leftViewTraversal(root.right, h_dist + 1, level + 1, values)


root = Tree(3)
root.left = Tree(9)
root.right = Tree(20)
root.right.left = Tree(15)
root.right.right = Tree(7)

print("printing left view of binary tree is: \n")
root.leftViewTraversal(root, root.h_dist, root.level, root.values)
for x in root.values.keys():
    root.result.append(root.values[x])

print(root.result)