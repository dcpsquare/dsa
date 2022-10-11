# Diagonal Traversal of a Binary tree

# Sol : start traverse from right and make h_dist as it is and 
# when traverse left make h_dist -1


class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.h_dist = 0
        self.level = 0
        self.values = {}
        self.result = []

    def digonalTraversal(self, root, h_dist, level, values):
        if root is None:
            return

        if h_dist in values:
            values[h_dist].append((level, root.data))
        else:
            values[h_dist] = [(level, root.data)]

        self.digonalTraversal(root.right, h_dist, level + 1, values)
        self.digonalTraversal(root.left, h_dist - 1, level + 1, values)

root = Tree(1)
root.right = Tree(3)
root.right.left = Tree(16)
root.right.right = Tree(6)
root.right.right.right = Tree(7)
root.left = Tree(2)
root.left.right = Tree(4)
root.left.right.right = Tree(5)
root.left.left = Tree(8)

root.digonalTraversal(root, root.h_dist, root.level, root.values)
print(root.values)
for x in root.values.keys():
    for column in sorted(root.values[x]): #here sorted used to sort level
        root.result.append(column[1])
print(root.result)