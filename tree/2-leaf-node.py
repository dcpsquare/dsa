#count Leaf Node

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def insert(self, data):
        if data:
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

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, end=" ")
        if self.right:
            self.right.printTree()

    def countLeafNodes(self, root):
        if root is None:
            return 0
        if root.left == None and root.right == None:
            return 1
        return self.countLeafNodes(root.left) + self.countLeafNodes(root.right)
        
    def levelOrder(self, root):
        from queue import Queue
        Q = Queue()
        Q.put(root)
        while(not Q.empty()):
            node = Q.get()
            if node == None:
                continue
            print(node.data, end=" ")
            Q.put(node.left)
            Q.put(node.right)
            
root = Tree(10)
root.insert(3)
root.insert(30)
root.insert(1)
root.insert(5)
root.insert(20)
root.insert(50)

print("\nprinting Tree Nodes: ")
root.printTree()

print("\n\nNo. of Leaf Nodes: ")
result = root.countLeafNodes(root)
print(result)

print("\n\nLevel Order traversal is: ")
root.levelOrder(root)

