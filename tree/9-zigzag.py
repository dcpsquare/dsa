# Binary Tree Zigzag Level Order Traversal

class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.data_list = []
        self.insert_level = []
        
    def levelorder(self,root):
        from queue import Queue
        Q = Queue()
        Q.put(root)
        leftToRight = True
        while not Q.empty():
            inner_list = []
            node = Q.get()
            if node is None:
                continue
            print(node.data, end=" ")
            inner_list.append(node.data)
            self.data_list.append(inner_list)
            if leftToRight is True:
                Q.put(node.right)
                Q.put(node.left)
                leftToRight =False
            else:
                Q.put(node.left)
                Q.put(node.right)
                leftToRight = True
        return self.data_list

        
root = Tree(3)
root.left = Tree(9)
root.right = Tree(20)
root.right.left = Tree(15)
root.right.right = Tree(7)

print("Printing in Level Order: \n")
ans = root.levelorder(root)
print(ans)