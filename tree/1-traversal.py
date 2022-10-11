class Tree:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    #insert node
    def insert(self,data):
        if self.data:
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

    def preOrder(self, root):#NLR
        res = []
        if root:
            res.append(root.data)
            res = res + self.preOrder(root.left)
            res = res + self.preOrder(root.right)
        return res

    def postOrder(self, root):#LRN
        res = []
        if root:
            res = res + self.postOrder(root.left)
            res = res + self.postOrder(root.right)
            res.append(root.data)
        return res

    def inOrder(self, root):#LNR
        res = []
        if root:
            res = res + self.inOrder(root.left)
            res.append(root.data)
            res = res + self.inOrder(root.right)
        return res

    def levelOrder(self, root):
        from queue import Queue
        Q = Queue()
        Q.put(root)
        while(not Q.empty()):
            node = Q.get()
            if node == None:
                continue
            print(node.data)
            Q.put(node.left)
            Q.put(node.right)

root = Tree(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
# print(root.preOrder(root))
# print(root.postOrder(root))
# print(root.inOrder(root))
print("Level Order traversal of the binary tree is: ")
root.levelOrder(root)