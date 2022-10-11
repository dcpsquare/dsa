# Sum of longest Bloodline of a tree
# Sol: Increse length value in every step and add node value in sum

class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.sum = 0
        self.length = 0
        self.ans = [0,0]

    def longestBloodline(self, root, sum, length, ans):
        if root is None:
            return

        sum += root.data
        length = length + 1
        ans[0] = max(ans[0], sum)
        ans[1] = max(ans[1], length)
        self.longestBloodline(root.left, sum, length, ans)
        self.longestBloodline(root.right, sum, length, ans)


root = Tree(4)
root.left = Tree(2)
root.left.left = Tree(7)
root.left.right = Tree(1)
root.left.right.left = Tree(6)
root.right = Tree(5)
root.right.left = Tree(2)
root.right.right = Tree(3)

print("Longest path from root to leaf: \n")
root.longestBloodline(root, root.sum, root.length, root.ans)
print(str(root.ans[0]) + " is highest sum and "+ str(root.ans[1]) + " is longest path")