# Verticle Order Tree Traversal

class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.h_dist = 0 #horizontal distance
        self.v_dist = 0 #level
        self.values = {}
        self.result = []

    def verticleTraversal(self, root, h_dist, v_dist, values):
        if root is None:
            return self.values
        
        if h_dist in values:
            values[h_dist].append((v_dist,root.data))
        else:
            values[h_dist] = [(v_dist, root.data)]

        self.verticleTraversal(root.left, h_dist - 1, v_dist + 1, values)
        self.verticleTraversal(root.right, h_dist + 1, v_dist + 1, values)

root = Tree(3)
root.left = Tree(9)
root.right = Tree(20)
root.right.left = Tree(15)
root.right.right = Tree(7)

root.verticleTraversal(root, root.h_dist, root.v_dist, root.values)
print("Verticle Order Tree Traversal is : \n")
for x in sorted(root.values.keys()):
    tmp = []
    for column in sorted(root.values[x]):
        tmp.append(column[1])
    root.result.append(tmp)
print(root.result)