# Construct a binary Tree Using InOrder/PreOrder 
# and print Output In PostOrder

class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def constructTree(InOrder, PreOrder, map_dict, PreOrderIndex, InOrderStart, InOrderEnd, n):
    if PreOrderIndex >= n or InOrderStart > InOrderEnd:
        return None
    

    root = Tree(PreOrder[PreOrderIndex])
    position  = map_dict[PreOrder[PreOrderIndex]]
    print(position)
    PreOrderIndex = PreOrderIndex + 1
    root.left = constructTree(InOrder, PreOrder, map_dict, PreOrderIndex, InOrderStart, position - 1, n)
    root.right = constructTree(InOrder, PreOrder, map_dict, PreOrderIndex, position + 1, InOrderEnd, n)
    return root

def postOrder(root):#LRN
        res = []
        if root:
            res = res + postOrder(root.left)
            res = res + postOrder(root.right)
            res.append(root.data)
        return res

if __name__ == "__main__":
    InOrder = [3, 1, 4, 0, 5, 2]
    PreOrder = [0, 1, 3, 4, 2, 5]
    PreOrderIndex = 0
    n = len(InOrder)
    map_dict = {}
    for key,val in enumerate(PreOrder):
        map_dict[val] = key
    ans = constructTree(InOrder, PreOrder, map_dict, PreOrderIndex, 0, n-1, n)
    new_ans = postOrder(ans)
    print(new_ans)