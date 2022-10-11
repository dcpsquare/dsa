# Flatten a binary tree into linked list

#Algorithm
'''
current = root
while current is not None:
    if current.left: #current left exist
        prev = current.left
        while prev.right:
            prev.right = current.right
            current.right = current.left
    current = current.left
'''

class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def flatten(self, root):
        current = root
        while current is not None:
            if current.left:
                print(current.data, end=" ")
                pred = current.left
                while pred.right is not None:
                    pred = pred.right
                    print(current.data, end=" ")
                pred.right = current.right
                current.right = current.left
                current.left = None
                # 
            current = current.right

root = Tree(1)
root.left = Tree(2)
root.left.left = Tree(3)
root.left.right = Tree(4)
root.right = Tree(5)
root.right.right = Tree(6)

root.flatten(root)