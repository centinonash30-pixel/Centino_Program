# Binary Tree using CENTINO

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree
root = Node("C")
root.left = Node("E")
root.right = Node("N1")

root.left.left = Node("T")
root.left.right = Node("I")

root.right.left = Node("N2")
root.right.right = Node("O")


# Breadth-First Search
def BFS(root):
    queue = [root]

    print("BFS Traversal:")

    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    print()


# Depth-First Search
def DFS(node):
    if node:
        print(node.data, end=" ")
        DFS(node.left)
        DFS(node.right)


# Display Results
BFS(root)

print("DFS Traversal:")
DFS(root)
print()