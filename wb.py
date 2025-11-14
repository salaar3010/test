from collections import deque

# Representation:
# 'S' = Start
# 'G' = Gold
# 'W' = Wumpus
# 'P' = Pit
# '.' = Empty

world = [
    ['S', '.', '.', 'P'],
    ['.', 'W', '.', '.'],
    ['.', '.', 'P', '.'],
    ['.', '.', '.', 'G']
]

n = len(world)

# Directions: up, down, left, right
moves = [(-1,0),(1,0),(0,-1),(0,1)]

def is_valid(x, y):
    """Check if a move is within grid and safe."""
    return 0 <= x < n and 0 <= y < n and world[x][y] not in ('W', 'P')

def bfs(start):
    """Breadth-First Search to find the shortest safe path to the gold."""
    queue = deque()
    queue.append((start, [start]))  # store current cell and path
    visited = set([start])
    
    while queue:
        (x, y), path = queue.popleft()
        
        # Found the gold
        if world[x][y] == 'G':
            return path
        
        # Explore all directions
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    
    return None

# Starting point (0,0)
start = (0, 0)
path = bfs(start)

if path:
    print("Gold found!")
    print("Shortest path to gold:", path)
else:
    print("No path to gold found.")
