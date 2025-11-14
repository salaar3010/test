# Wumpus World DFS Solver

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
visited = [[False]*n for _ in range(n)]
path = []

# Directions: up, down, left, right
moves = [(-1,0),(1,0),(0,-1),(0,1)]

def is_valid(x, y):
    """Check if a move is valid within the grid and safe."""
    return 0 <= x < n and 0 <= y < n and world[x][y] not in ('W','P')

def dfs(x, y):
    """Depth-First Search to find gold."""
    if not is_valid(x, y) or visited[x][y]:
        return False
    
    visited[x][y] = True
    path.append((x, y))
    
    # Found gold
    if world[x][y] == 'G':
        return True

    # Explore all directions
    for dx, dy in moves:
        if dfs(x+dx, y+dy):
            return True
    
    # Backtrack if dead end
    path.pop()
    return False

# Start DFS from the start cell (0,0)
found = dfs(0, 0)

if found:
    print(" Gold found!")
    print("Path to gold:", path)
else:
    print(" No path to gold found.")
