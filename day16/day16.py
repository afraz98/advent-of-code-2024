import heapq, math, timeit
direction_markers = ["^", "v", ">", "<"]

class Cell:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data
        self.f = math.inf
        self.g = math.inf
        self.h = math.inf
        self.parent_x = -1
        self.parent_y = -1
        self.direction = 2 # East
        pass

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

def parse_input(filename):
    return [[x for x in line.strip("\n")] for line in open(filename, 'r')]

def print_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            print(grid[row][col], end='')
        print()

def euclidean_distance(x2, x1, y2, y1):
    return math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))

def manhattan_distance(x2, x1, y2, y1):
    return abs(x2 - x1) + abs(y2 - y1)

def get_new_direction(x_new, x, y_new, y):
    if x > x_new:
        return 0
    if x_new > x:
        return 1
    if y_new > y:
        return 2
    return 3

def get_rotation_cost(current_dir, new_dir):
    diff = abs(current_dir - new_dir) % 4
    return 1000 * (1 if diff > 0 else 0)

def trace_path(cells, end_x, end_y):
    """
    Trace A* algorithm path, returning path score

    Args:
        cells (list): Cell data matrix
        end_x (int): Ending x coordinate
        end_y (int): Ending y coordinate

    Returns:
        (int): Path score
    """    
    path_score = 0
    row, col = end_x, end_y
    path = []

    while not (cells[row][col].parent_x == row and cells[row][col].parent_y == col):
        path.insert(0, cells[row][col])
        parent_row, parent_col = cells[row][col].parent_x, cells[row][col].parent_y 
        path_score = path_score + 1.0 + get_rotation_cost(cells[row][col].direction, cells[parent_row][parent_col].direction) 
        row, col = parent_row, parent_col

    path.insert(0, cells[row][col])
    return int(path_score)


def traverse_maze_part_one(start_x, start_y, end_x, end_y, grid, height, width):
    """
    Modified A* search algorithm.

    Args:
        start_x (int): Starting x coordinate
        start_y (int): Starting y coordinate
        end_x (int): End x coordinate
        end_y (int): End y coordinate
        grid (list(list(str))): Maze as a 2D array of strings
        height (int): Maze height
        width (int): Maze width
    Returns:
        (list): Path score (1 for each cell traveled + 1000 if turn necessary)
    """
    open = []
    closed = [[False for i in range(width)] for i in range(height)]
    cells = [[Cell(i, j, grid[i][j]) for j in range(width)] for i in range(height)]
    closed = [[False for _ in range(width)] for _ in range(height)]

    start_cell = cells[start_x][start_y]
    start_cell.f = 0.0
    start_cell.g = 0.0
    start_cell.h = 0.0
    start_cell.parent_x = start_x
    start_cell.parent_y = start_y
    open.append(start_cell)

    while open:
        cell = min(open, key=lambda x : x.f)
        open.remove(cell)
        closed[cell.x][cell.y] = True

        if cell.x == end_x and cell.y == end_y: # End found
            return trace_path(cells, end_x, end_y)
        
        for dx, dy, new_direction in [(-1, 0, 0), (1, 0, 1), (0, 1, 2), (0, -1, 3)]: # N S E W
            new_x = cell.x + dx
            new_y = cell.y + dy

            if 0 <= new_x < height and 0 <= new_y < width: # Cell within grid bounds
                if closed[new_x][new_y]: # Successor not in closed list and path is 'unblocked'
                    continue

                if grid[cell.x][cell.y] != "#":
                    g_new = cells[cell.x][cell.y].g + 1.0 + get_rotation_cost(cell.direction, new_direction)
                    h_new = manhattan_distance(new_x, end_x, new_y, end_y) 
                    f_new = g_new + h_new
                    if cells[new_x][new_y].f == math.inf or cells[new_x][new_y].f > f_new:
                        cells[new_x][new_y].f = f_new
                        cells[new_x][new_y].g = g_new
                        cells[new_x][new_y].h = h_new
                        cells[new_x][new_y].parent_x = cell.x
                        cells[new_x][new_y].parent_y = cell.y
                        cells[new_x][new_y].direction = new_direction
                        open.append(cells[new_x][new_y])
    return -1

def solve_part_one():
    grid = parse_input("day16.txt")

    width = len(grid[0])
    height = len(grid)

    start_x, start_y = 0, 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 'S':
                start_x, start_y = i, j

    end_x, end_y = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'E':
                end_x, end_y = i, j
    print(traverse_maze_part_one(start_x, start_y, end_x, end_y, grid, height, width))


def traverse_maze_part_two(start_x, start_y, end_x, end_y, grid, height, width):
    """
    Breadth-first traversal. Inspired by solution posted by u/wurlin_murlin

    Args:
        start_x (int): Starting x coordinate
        start_y (int): Starting y coordinate
        end_x (int): End x coordinate
        end_y (int): End y coordinate
        grid (list(list(str))): Maze as a 2D array of strings
        height (int): Maze height
        width (int): Maze width
    Returns:
        (list): Path score (1 for each cell traveled + 1000 if turn necessary)
    """
    paths = []                                                 # All possible paths to the ending coordinates
    cells = [(0, (start_y, start_x, 2), [(start_y, start_x)])] # Cells to visit (starting from start coordinates)
    best_score = math.inf
    
    # Score for each tile in the grid for each direction it is visited from
    visited = [[[math.inf for _ in range(len(direction_markers))] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    while cells and cells[0][0] <= best_score:
        score, (y, x, direction), path = heapq.heappop(cells) # Operate on cell list like min-heap

        if x == end_x and y == end_y: # End found
            best_score = score
            paths.append(path)
            continue

        if visited[y][x][direction] < score:
            continue
        visited[y][x][direction] = score

        for dx, dy, new_direction in [(-1, 0, 0), (1, 0, 1), (0, 1, 2), (0, -1, 3)]: # N S E W
            new_y, new_x = y + dy, x + dx
            if grid[new_y][new_x] != '#' and (new_y, new_x) not in path:
                heapq.heappush(cells, (score + 1.0 + get_rotation_cost(direction, new_direction), (new_y, new_x, new_direction), path + [(new_y, new_x)]))
    return paths

def solve_part_two():
    grid = parse_input("day16.txt")
    width = len(grid[0])
    height = len(grid)
    positions = set()

    start_x, start_y = 0, 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 'S':
                start_x, start_y = i, j

    end_x, end_y = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'E':
                end_x, end_y = i, j

    paths = traverse_maze_part_two(start_x, start_y, end_x, end_y, grid, height, width)

    for path in paths:
        positions = positions | set(path)
    print(len(positions))
    
result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))

