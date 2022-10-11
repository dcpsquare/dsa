# k sum path

class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.count = 0
        self.path = []


    def countKPath(self, root, k):
        if root is None:
            return
        print("AAA")
        self.path.append(root.data)
        self.countKPath(root.left, k)
        self.countKPath(root.right, k)
        print(root.data)
        # print(self.path) # how list look like on every node when return
        # sum = 0
        # size = len(self.path)
        # for x in range(size-1, 0, -1):
        #     sum+=self.path[x]
        #     if sum == k:
        #         self.count+=1
        # self.path.pop()

# root = Tree(1)
# root.left = Tree(3)
# root.right = Tree(-1)
# root.left.left = Tree(2)
# root.left.right = Tree(1)
# root.left.right.left = Tree(1)
# root.right.left = Tree(4)
# root.right.left.left = Tree(1)
# root.right.left.right = Tree(2)
# root.right.right = Tree(5)
# root.right.right.right = Tree(6)

root = Tree(1)
root.left = Tree(2)
root.left.left = Tree(4)
root.left.left.left = Tree(1)
root.right = Tree(3)
root.left.right = Tree(21)
k = 5
root.countKPath(root, k)
print(root.count)