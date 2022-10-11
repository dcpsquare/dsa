# Longest Common Ancestor of Binary Tree - LCA

from dataclasses import dataclass


class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def findLCA(self, root, n1, n2):
        if root is None:
            return
        
        if root.data is n1 or root.data is n2:
            return root.data

        left_ans = self.findLCA(root.left, n1, n2)
        right_ans = self.findLCA(root.right, n1, n2)

        if left_ans is not None and right_ans is not None:
            return root.data
        elif left_ans is not None and right_ans is None:
            return left_ans
        elif left_ans is None and right_ans is not None:
            return right_ans
        else:
            return None

root = Tree(5)
root.left = Tree(4)
root.left.left = Tree(7)
root.left.right = Tree(8)
root.left.right.left = Tree(12)
root.left.right.right = Tree(9)
root.right = Tree(3)
root.right.right = Tree(27)
root.right.left = Tree(22)
root.right.right.left = Tree(29)
n1 = 8
n2 = 27
ans = root.findLCA(root, n1, n2)
print(ans)