print("Depth First Search (DFS)")

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}

visited = []
stack = []

def dfs(start):
    stack.append(start)
    visited.append(start)

    while stack:
        node = stack.pop()
        print(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

dfs('A')