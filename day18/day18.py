import math, timeit

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
        self.direction = 2
        pass

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

def manhattan_distance(x2, x1, y2, y1):
    return abs(x2 - x1) + abs(y2 - y1)

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
        parent_row = cells[row][col].parent_x
        parent_col = cells[row][col].parent_y 
        path_score = path_score + 1.0
        row, col = parent_row, parent_col

    path.insert(0, cells[row][col])
    return int(path_score)

def traverse_grid(start_x, start_y, end_x, end_y, grid, height, width):
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
        (list): Path score (1 for each cell traveled)
    """
    open = []
    closed = [[False for i in range(width)] for i in range(height)]
    cells = [[None for i in range(width)] for i in range(height)]
    score = 0

    for i in range(height):
        for j in range(width):
            cells[i][j] = Cell(i, j, grid[i][j])

    start_cell = cells[start_x][start_y]
    start_cell.f = 0.0
    start_cell.g = 0.0
    start_cell.h = 0.0
    start_cell.parent_x = start_x
    start_cell.parent_y = start_y
    open.append(start_cell)

    while open:
        # cell = open.pop(0) # Try dequeuing minimum f value?...
        cell = min(open, key=lambda x : x.f)
        open.remove(cell)
        closed[cell.x][cell.y] = True

        if cell.x == end_x and cell.y == end_y: # End found
            return trace_path(cells, end_x, end_y)
        
        for dx, dy, new_direction in [(-1, 0, 0), (1, 0, 1), (0, 1, 2), (0, -1, 3)]: # N S E W
            new_x = cell.x + dx
            new_y = cell.y + dy

            if 0 <= new_x < height and 0 <= new_y < width: # Cell within grid bounds
                # Successor not in closed list and path is 'unblocked'
                if closed[new_x][new_y]:
                    continue

                if grid[cell.x][cell.y] != "#":
                    g_new = cells[cell.x][cell.y].g + 1.0
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
    return score

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def print_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            print(grid[row][col], end='')
        print()

def solve_part_one():
    width, height = 71, 71
    grid = [['.' for col in range(width)] for row in range(height)]

    start_x, start_y = 0, 0
    end_x, end_y = 70, 70

    bytes = parse_input("day18.txt")
    print(bytes)
    for i in range(1024):
        if len(bytes[i]) > 1:
            x,y = bytes[i].split(",")
            grid[int(y)][int(x)] = '#'
    print_grid(grid)
    print(traverse_grid(start_x, start_y, end_x, end_y, grid, height, width))
    pass

def solve_part_two():
    width, height = 71, 71
    grid = [['.' for col in range(width)] for row in range(height)]

    start_x, start_y = 0, 0
    end_x, end_y = 70, 70

    bytes = parse_input("day18.txt")
    print(bytes)
    for i in range(1024):
        if len(bytes[i]) > 1:
            x,y = bytes[i].split(",")
            grid[int(y)][int(x)] = '#'

    i = 1024
    path_score = traverse_grid(start_x, start_y, end_x, end_y, grid, height, width)
    while path_score > 0:
        if len(bytes[i]) > 1:
            x,y = bytes[i].split(",")
            print(x,y)
            grid[int(y)][int(x)] = '#'
        i = i + 1
        path_score = traverse_grid(start_x, start_y, end_x, end_y, grid, height, width)
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
