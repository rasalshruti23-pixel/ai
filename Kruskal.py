print("Kruskal Algorithm")

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    parent[y_root] = x_root

def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])
    parent = []

    for i in range(vertices):
        parent.append(i)

    mst = []
    total_cost = 0

    for u, v, w in edges:
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            mst.append((u, v, w))
            total_cost += w
            union(parent, x, y)

    return mst, total_cost

vertices = 5
edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7)
]

mst, cost = kruskal(vertices, edges)

print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(u, "-", v, ":", w)

print("Total Cost:", cost)