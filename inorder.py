
# INORDER TRAVERSAL
# Last Name: CENTINO

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree
root = Node("C")
root.left = Node("E")
root.right = Node("N")

root.left.left = Node("T")
root.left.right = Node("I")

root.right.left = Node("N")
root.right.right = Node("O")


def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


print("INORDER TRAVERSAL:")
inorder(root)
print()
