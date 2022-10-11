class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def createBST(self, data):
        if self.data is None:
            self.data = data
        if self.data and data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.createBST(data)
        elif self.data and data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.createBST(data)
        else:
            self.data = data

    def inOrderTraverse(self,root):
        res = []
        res = res + self.inOrderTraverse(root.left)
        res.append(root.data)
        res = res + self.inOrderTraverse(root.right)
        return res

bst_list = [10, 8, 21, 7, 27, 5, 4, 3]
root = Node(None)
for x in bst_list:
    root.createBST(x)

ans = root.inOrderTraverse(root)
print(ans)
