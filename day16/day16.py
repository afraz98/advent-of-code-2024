import math, timeit

direction_markers = ["^", "v", ">", "<", "?"]

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
        self.direction = 4
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

def get_new_direction(x_new, x, y_new, y):
    if x > x_new:
        return 0
    if x_new > x:
        return 1
    if y_new > y:
        return 2
    return 3

def trace_path(grid, cells, end_x, end_y):
    """
    Trace A* algorithm path, returning path length

    Args:
        cells (list): Cell data matrix
        end_x (int): Ending x coordinate
        end_y (int): Ending y coordinate

    Returns:
        (int): Path length
    """    
    path_score = 0
    row = end_x
    col = end_y
    path = []

    while not (cells[row][col].parent_x == row and cells[row][col].parent_y == col):
        path.insert(0, cells[row][col])
        path_score += 1.0 if get_new_direction(cells[row][col].parent_x, row, cells[row][col].parent_y, col) == cells[row][col].direction else 1000.0
        new_row = cells[row][col].parent_x 
        new_col = cells[row][col].parent_y
        row = new_row
        col = new_col
        grid[cells[row][col].x][cells[row][col].y] = direction_markers[cells[row][col].direction]

    print_grid(grid)
    path.insert(0, cells[row][col])
    return path_score

def traverse_maze(start_x, start_y, end_x, end_y, grid, height, width):
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
        (list): Path score (1 for each cell traveled + 1000 for each turn)
    """

    open = []
    closed = [[False for i in range(width)] for i in range(height)]
    cells = [[None for i in range(width)] for i in range(height)]
    score = 0

    for i in range(height):
        for j in range(width):
            cells[i][j] = Cell(i, j, grid[i][j])

    cells[start_x][start_y].f = 0.0
    cells[start_x][start_y].g = 0.0
    cells[start_x][start_y].h = 0.0
    cells[start_x][start_y].parent_x = start_x
    cells[start_x][start_y].parent_y = start_y
    open.append(cells[start_x][start_y])

    while open != []:
        cell = open.pop(0)
        closed[cell.x][cell.y] = True
        for new_x,new_y in [(cell.x - 1, cell.y), (cell.x + 1, cell.y), (cell.x, cell.y + 1), (cell.x, cell.y - 1)]: # N S E W
            if 0 <= new_x < height and 0 <= new_y < width: # Cell within grid bounds
                if new_x == end_x and new_y == end_y and grid[new_x][new_y] != "#": # Successor is destination cell?
                    cells[new_x][new_y].parent_x = cell.x
                    cells[new_x][new_y].parent_y = cell.y
                    return trace_path(grid, cells, end_x, end_y)

                # Successor not in closed list and path is 'unblocked'
                elif not closed[new_x][new_y] and grid[cell.x][cell.y] != "#":
                    g_new = cells[cell.x][cell.y].g + 1.0
                    h_new = euclidean_distance(cell.x, new_y, cell.y, end_y) + 1000.0 if get_new_direction(new_x, cell.x, new_y, cell.y) != cells[cell.x][cell.y].direction else 0.0
                    f_new = g_new + h_new
                    if cells[new_x][new_y].f == math.inf or cells[new_x][new_y].f > f_new:
                        cells[new_x][new_y].f = f_new
                        cells[new_x][new_y].g = g_new
                        cells[new_x][new_y].h = h_new
                        cells[new_x][new_y].parent_x = cell.x
                        cells[new_x][new_y].parent_y = cell.y
                        cells[new_x][new_y].direction = get_new_direction(new_x, cell.x, new_y, cell.y)
                        open.append(cells[new_x][new_y])
    return score

def solve_part_one():
    grid = parse_input("day16_test.txt")

    width = len(grid[0])
    height = len(grid)

    start_x = 0
    start_y = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 'S':
                start_x = i
                start_y = j

    end_x = 0
    end_y = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'E':
                end_y = j
                end_x = i
    print(traverse_maze(start_x, start_y, end_x, end_y, grid, height, width))

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))

