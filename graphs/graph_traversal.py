#Import inbuilt collection
from collections import deque

# Define graph structure
graph = {
    0: [1, 4],
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}

def depth_first_search(graph, start):
    # define visited variable
    visited = set()
    stack = [start]

    while stack: # iterate while stack has nodes
        node = stack.pop()
        if not node in visited:
            # perform operation with the node
            print('Now visiting', node)
        visited.add(node)
        # Check the neighbor nodes
        for neighbor in graph[node]:
            if not neighbor in visited:
                stack.append(neighbor)
    return visited

def bredth_first_search(graph, start):
    # visited variable
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if not node in visited:
            # perform visited operation
            print("Now visiting", node)
        visited.add(node)

        # check the neighbors node
        for neighbor in graph[node]:
            if not neighbor in visited:
                queue.append(neighbor)
    return visited


if __name__ == "__main__":
    # execute DFS method
    # depth_first_search(graph, 0)
    bredth_first_search(graph, 0)