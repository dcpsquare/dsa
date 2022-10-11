# Is Identical Tree or same tree

from unittest import result


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

def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None and root2 is not None:
        return False
    if root1 is not None and root2 is None:
        return False
    left = isIdentical(root1.left, root2.left)
    right = isIdentical(root1.right, root2.right)
    value = root1.data == root2.data

    if left and right and value:
        return True
    else:
        return False

root1 = Tree(1)
root1.insert(2)
root1.insert(2)

root2 = Tree(1)
root2.insert(2)
root2.insert(2)


if __name__ == "__main__":
  if isIdentical(root1, root2):
      print("Both trees are identical")
  else:
      print("Trees are not identical")