class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.pair = [0,0]

    def maxSumNonAdjacentNode(self, root):
        if root is None:
            return self.pair

        left_pair = self.maxSumNonAdjacentNode(root.left)
        right_pair = self.maxSumNonAdjacentNode(root.right)
        
        new_pair = [0,0]
        new_pair[0] = root.data + left_pair[1] + right_pair[1]
        new_pair[1] = max(left_pair[0] , left_pair[1]) + max(right_pair[0] , right_pair[1])
        # print(new_pair, left_pair[0] , left_pair[1] , right_pair[0] , right_pair[1])
        return new_pair

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.right.left = Tree(5)
root.right.right = Tree(6)

ans = root.maxSumNonAdjacentNode(root)
print(max(ans))