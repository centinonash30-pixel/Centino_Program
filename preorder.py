
# PREORDER TRAVERSAL
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


def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


print("PREORDER TRAVERSAL:")
preorder(root)
print()
