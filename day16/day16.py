import math, timeit

class Cell:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data

        self.f = 999.0
        self.g = 999.0
        self.h = 999.0
        self.parent_x = -1
        self.parent_y = -1
        pass

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

def parse_input(filename):
    return [[x for x in line.strip("\n")] for line in open(filename, 'r')]

def trace_path(cells, end_x, end_y):
    """
    Trace A* algorithm path, returning path length

    Args:
        cells (list): Cell data matrix
        end_x (int): Ending x coordinate
        end_y (int): Ending y coordinate

    Returns:
        (int): Path length
    """
    path_len = 0
    
    row = end_x
    col = end_y
    path = []
    while not (cells[row][col].parent_x == row and cells[row][col].parent_y == col):
        path.insert(0, cells[row][col])

        new_row = cells[row][col].parent_x 
        new_col = cells[row][col].parent_y

        row = new_row
        col = new_col

    path.insert(0, cells[row][col])
    return path

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
        (list): Path
    """

    open = []
    closed = [[False for i in range(width)] for i in range(height)]
    cells = [[None for i in range(width)] for i in range(height)]
    path_score = 0

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

        # 'North' successor
        # Cell within grid bounds
        if 0 <= cell.x - 1 < height and 0 <= cell.y < width:
                # 'North' successor is destination cell?
                if cell.x - 1 == end_x and cell.y == end_y and grid[cell.x][cell.y] != "#":
                    cells[cell.x - 1][cell.y].parent_x = cell.x
                    cells[cell.x - 1][cell.y].parent_y = cell.y
                    return trace_path(cells, end_x, end_y)

                # Successor not in closed list and path is 'unblocked'
                elif closed[cell.x - 1][cell.y] == False and grid[cell.x][cell.y] != "#":
                    g_new = cells[cell.x][cell.x].g + 1.0
                    h_new = math.sqrt((cell.x - end_x)*(cell.x - end_x)+(cell.y - end_y)*(cell.y - end_y))
                    f_new = g_new + h_new
                    
                    if cells[cell.x - 1][cell.y].f == 999.0 or cells[cell.x - 1][cell.y].f > f_new:
                        cells[cell.x - 1][cell.y].f = f_new
                        cells[cell.x - 1][cell.y].g = g_new
                        cells[cell.x - 1][cell.y].h = h_new
                        cells[cell.x - 1][cell.y].parent_x = cell.x
                        cells[cell.x - 1][cell.y].parent_y = cell.y
                        open.append(cells[cell.x - 1][cell.y])
        
        # 'South' successor
        # Cell within grid bounds
        if 0 <= cell.x + 1 < height and 0 <= cell.y < width:
                # 'South successor is destination cell?
                if cell.x + 1 == end_x and cell.y == end_y and grid[cell.x][cell.y] != "#":
                    cells[cell.x + 1][cell.y].parent_x = cell.x
                    cells[cell.x + 1][cell.y].parent_y = cell.y
                    return trace_path(cells, end_x, end_y)
                
                # Successor not in closed list and path is 'unblocked'
                elif closed[cell.x + 1][cell.y] == False and grid[cell.x][cell.y] != "#":
                    g_new = cells[cell.x][cell.x].g + 1.0
                    h_new = math.sqrt((cell.x - end_x)*(cell.x - end_x)+(cell.y - end_y)*(cell.y - end_y))
                    f_new = g_new + h_new
                    
                    if cells[cell.x + 1][cell.y].f == 999.0 or cells[cell.x + 1][cell.y].f > f_new:
                        cells[cell.x + 1][cell.y].f = f_new
                        cells[cell.x + 1][cell.y].g = g_new
                        cells[cell.x + 1][cell.y].h = h_new
                        cells[cell.x + 1][cell.y].parent_x = cell.x
                        cells[cell.x + 1][cell.y].parent_y = cell.y
                        open.append(cells[cell.x + 1][cell.y])

        # 'East' successor
        # Cell within grid bounds
        if 0 <= cell.x < height and 0 <= cell.y + 1 < width:
                # 'South successor is destination cell?
                if cell.x == end_x and cell.y + 1 == end_y and grid[cell.x][cell.y] != "#":
                    # print("Found destination")
                    cells[cell.x][cell.y + 1].parent_x = cell.x
                    cells[cell.x][cell.y + 1].parent_y = cell.y
                    return trace_path(cells, end_x, end_y)
 
                # Successor not in closed list and path is 'unblocked'
                elif closed[cell.x][cell.y + 1] == False and grid[cell.x][cell.y] != "#":
                    g_new = cells[cell.x][cell.x].g + 1.0
                    h_new = math.sqrt((cell.x - end_x) * (cell.x - end_x) + (cell.y - end_y) * (cell.y - end_y))
                    f_new = g_new + h_new
                    
                    if cells[cell.x][cell.y + 1].f == 999.0 or cells[cell.x][cell.y + 1].f > f_new:
                        cells[cell.x][cell.y + 1].f = f_new
                        cells[cell.x][cell.y + 1].g = g_new
                        cells[cell.x][cell.y + 1].h = h_new
                        cells[cell.x][cell.y + 1].parent_x = cell.x
                        cells[cell.x][cell.y + 1].parent_y = cell.y
                        open.append(cells[cell.x][cell.y + 1])

        # 'West' successor
        # Cell within grid bounds
        if 0 <= cell.x < height and 0 <= cell.y - 1 < width:
                # 'South successor is destination cell?
                if cell.x == end_x and cell.y - 1 == end_y and grid[cell.x][cell.y] != "#":
                    cells[cell.x][cell.y - 1].parent_x = cell.x
                    cells[cell.x][cell.y - 1].parent_y = cell.y
                    return trace_path(cells, end_x, end_y)
                
                # Successor not in closed list and path is 'unblocked'
                elif closed[cell.x][cell.y - 1] == False and grid[cell.x][cell.y] != "#":
                    g_new = cells[cell.x][cell.x].g + 1.0
                    h_new = math.sqrt((cell.x - end_x)*(cell.x - end_x)+(cell.y - end_y)*(cell.y - end_y))
                    f_new = g_new + h_new
                    
                    if cells[cell.x][cell.y - 1].f == 999.0 or cells[cell.x][cell.y - 1].f > f_new:
                        cells[cell.x][cell.y - 1].f = f_new
                        cells[cell.x][cell.y - 1].g = g_new
                        cells[cell.x][cell.y - 1].h = h_new
                        cells[cell.x][cell.y - 1].parent_x = cell.x
                        cells[cell.x][cell.y - 1].parent_y = cell.y
                        open.append(cells[cell.x][cell.y - 1])
    return []

# Probably need to implement A* as with previous years.
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
    path = traverse_maze(start_x, start_y, end_x, end_y, grid, height, width)
    for block in path:
        print(block.x, block.y)

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))

