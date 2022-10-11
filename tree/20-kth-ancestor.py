#Kth Ancestor in a tree

class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.k = 2

    def findKthAncestor(self, root, n):
        if root is None:
            return
        
        if root.data is n:
            return root.data

        left = self.findKthAncestor(root.left, n)
        right = self.findKthAncestor(root.right, n)

        if left is not None and right is None:
            self.k=self.k-1
            if self.k <= 0:
                # lock ans
                self.k = 999999
                return root.data
            return left

        if right is not None and left is None:
            self.k=self.k-1
            if self.k <= 0:
                # lock ans
                self.k = 999999
                return root.data
            return right
        return None


root = Tree(1)
root.left = Tree(2)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right = Tree(3)

n = 4

ans = root.findKthAncestor(root, n)
if ans is None or ans is n:
    print(-1)
else:
    print(ans)