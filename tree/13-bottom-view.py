class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.h_dist = 0
        self.level = 0
        self.values = {}
        self.result = []

    def bottomOrderTraversal(self, root, h_dist, level, values):
        if root is None:
            return
        
        if h_dist in values:
            values[h_dist].append((level, root.data))
        else:
            values[h_dist] = [(level, root.data)]

        self.bottomOrderTraversal(root.left, h_dist - 1, level + 1, values)
        self.bottomOrderTraversal(root.right, h_dist + 1, level + 1, values)

root = Tree(3)
root.left = Tree(9)
root.right = Tree(20)
root.right.left = Tree(15)
root.right.right = Tree(7)


print("printing bottom order traversal: \n")

root.bottomOrderTraversal(root, root.h_dist, root.level, root.values)
print(root.values)
for x in sorted(root.values.keys()):
    temp = None
    for column in root.values[x]:
        temp = column[1]
    root.result.append(temp)
print(root.result)