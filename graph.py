# Graph using CENTINO

graph = {
    "C": ["E", "N1"],
    "E": ["C", "T", "I"],
    "N1": ["C", "N2", "O"],
    "T": ["E", "I"],
    "I": ["E", "T", "N2"],
    "N2": ["N1", "I"],
    "O": ["N1"]
}


# Breadth-First Search
def BFS(graph, start):
    visited = []
    queue = [start]

    print("BFS Traversal:")

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            print(node, end=" ")

            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    print()


# Depth-First Search
def DFS(graph, node, visited):
    if node not in visited:
        visited.append(node)
        print(node, end=" ")

        for neighbor in graph[node]:
            DFS(graph, neighbor, visited)


# Display Results
BFS(graph, "C")

print("DFS Traversal:")
DFS(graph, "C", [])
print()