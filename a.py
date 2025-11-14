import networkx as nx
import matplotlib.pyplot as plt
import queue

def bfs(graph, start):
    visited = set()
    q = queue.Queue()
    q.put(start)
    bfs_order = []
    edges_traversed = []

    while not q.empty():
        node = q.get()
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    q.put(neighbor)
                    edges_traversed.append((node, neighbor))
    return bfs_order, edges_traversed

def dfs(graph, start):
    visited = set()
    stack = [start]

    dfs_order = []
    edges_traversed = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            dfs_order.append(node)

            # Add neighbors in reverse so left-most is processed first
            for neighbor in reversed(list(graph.neighbors(node))):
                if neighbor not in visited:
                    stack.append(neighbor)
                    edges_traversed.append((node, neighbor))

    return dfs_order, edges_traversed

import heapq

def ucs(graph, start):
    visited = set()
    pq = [(0, start)]   # (cost, node)

    ucs_order = []
    edges_traversed = []
    cost_so_far = {start: 0}

    while pq:
        cost, node = heapq.heappop(pq)

        if node not in visited:
            visited.add(node)
            ucs_order.append(node)

            for neighbor in graph.neighbors(node):
                weight = graph[node][neighbor].get("weight", 1)
                new_cost = cost + weight

                if neighbor not in visited and (neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]):
                    cost_so_far[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))
                    edges_traversed.append((node, neighbor))

    return ucs_order, edges_traversed

def plot_collaboration_graph(graph, path=None):
    """Plot the collaboration graph using NetworkX."""
    G = nx.Graph(graph)
    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 8))
    nx.draw(
        G, pos, with_labels=True, node_color='lightblue', node_size=2000,
        font_size=10, font_weight='bold', edge_color='gray'
    )

    # Highlight the shortest path
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange')
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.title("Department Collaboration Network", fontsize=14)
    plt.show()


import math

def haversine(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))

    R = 6371  # Radius of Earth in kilometers
    return R * c


menu ='''Select the search algorithm:
1. Breadth-First Search (BFS)
2. Depth-First Search (DFS)
3. Uniform Cost Search (UCS)'''

print(menu)
choice = input("Enter choice (1/2/3): ")
G = nx.Graph()
G.add_weighted_edges_from([
    ('A','B',4), ('A','D',4), ('A','E',6), ('A','F',4),
    ('B','C',6), ('B','D',8), ('B','E',8), ('B','F',4), ('B','G',7),
    ('C','D',4), ('C','E',8), ('C','F',6),
    ('D','E',8), ('D','F',6),
    ('E','G',7),
    ('F','G',5)
])
start_node = "A"
goal = "F"
if choice == '1':
    order, edges_traversed = bfs(G, start_node)
    print("BFS Order of traversal:", order)
elif choice == '2':
    order, edges_traversed = dfs(G, start_node)
    print("DFS Order of traversal:", order)
elif choice == '3':
    order, edges_traversed = ucs(G, start_node)
    print("UCS Order of traversal:", order)


# Extract the path to the goal
path = []
if goal in order:
    index = order.index(goal)
    path = order[:index + 1]    
    print("Path to goal:", path)
    # Plot the collaboration graph with the path highlighted
    plot_collaboration_graph(G, path)


#for caculating distance
import networkx as nx
import matplotlib.pyplot as plt
import math

hubs = {
    "A": (12.9716, 77.5946),
    "B": (13.0827, 80.2027),
    "C": (11.0168, 76.9558),
    "D": (9.9252, 78.1198),
    "E": (17.3850, 78.1198),
    "F": (15.8281, 78.0373),
    "G": (10.7905, 78.7047)
}

def euclidean(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

G = nx.Graph()

# Add nodes + weighted edges
for h1 in hubs:
    for h2 in hubs:
        if h1 != h2:
            (lat1, lon1) = hubs[h1]
            (lat2, lon2) = hubs[h2]
            dist = euclidean(lat1, lon1, lat2, lon2)
            G.add_edge(h1, h2, weight=dist)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue")
plt.show()


