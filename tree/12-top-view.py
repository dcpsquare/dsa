class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.h_dist = 0
        self.level = 0
        self.values = {}
        self.result = []

    def topViewTraversal(self, root, h_dist, level, values):
        if root is None:
            return
        
        if h_dist in self.values:
            pass
        else:
            values[h_dist] = [(level, root.data)]

        self.topViewTraversal(root.left, h_dist - 1, level + 1, values)
        self.topViewTraversal(root.right, h_dist + 1, level + 1, values)




root = Tree(3)
root.left = Tree(9)
root.right = Tree(20)
root.right.left = Tree(15)
root.right.right = Tree(7)

print("printing to view of tree: \n")
root.topViewTraversal(root, root.h_dist, root.level, root.values)
print(root.values)

for x in sorted(root.values.keys()):
    column = root.values[x]
    root.result.append(column[0][1])
print(root.result)