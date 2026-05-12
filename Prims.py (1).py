import heapq

print("Prim's Algorithm")

def prims_mst(graph, start):
    visited = set()
    min_heap = [(0, start, -1)]
    mst = []
    total_cost = 0

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)

        if current in visited:
            continue

        visited.add(current)

        if parent != -1:
            mst.append((parent, current, weight))
            total_cost += weight

        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return mst, total_cost

graph = {
    0: [(1,4),(3,6)],
    1: [(0,4),(2,3),(3,8),(4,5)],
    2: [(1,3),(4,2)],
    3: [(0,6),(1,8)],
    4: [(1,5),(2,2)]
}

mst, cost = prims_mst(graph, 0)

print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(u, "-", v, ":", w)

print("Total Cost:", cost)