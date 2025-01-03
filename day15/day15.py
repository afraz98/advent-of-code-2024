import timeit

velocity = {
    '<': (0, -1),
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0)
}

def print_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            print(grid[row][col], end='')
        print()

def parse_input(filename):
    return [line for line in open(filename, 'r')]

def move_box(grid, x, y, dx, dy):
    if grid[y+dy][x+dx] == '#':
        return False
    if grid[y+dy][x+dx] == 'O':
        if move_box(grid, x+dx, y+dy, dx, dy):
            grid[y+dy][x+dx] = 'O'
            grid[y][x] = '.'
            return True
        return False
    grid[y+dy][x+dx] = 'O'
    grid[y][x] = '.'
    return True

def parse_instructions(grid, instruction, robot_x, robot_y):
    dy, dx = velocity[instruction]
    if grid[robot_y + dy][robot_x + dx] == '#': # Wall in new position
        return robot_x, robot_y
    if grid[robot_y + dy][robot_x + dx] == 'O': # Box in new position
        if move_box(grid, robot_x + dx, robot_y + dy, dx, dy):
            grid[robot_y + dy][robot_x + dx] = '@'
            grid[robot_y][robot_x] = '.'
            return robot_x + dx, robot_y + dy
        return robot_x, robot_y
    grid[robot_y + dy][robot_x + dx] = '@'
    grid[robot_y][robot_x] = '.'
    return robot_x + dx, robot_y + dy

def solve_part_one():
    input = parse_input("day15.txt")
    grid, instructions = ''.join(input).split("\n\n")
    grid = [[col for col in row.strip('\n')] for row in grid.split('\n')]
    instructions = [str(instruction) for instruction in instructions.replace('\n', "")]

    robot_x, robot_y = -1, -1
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                robot_x, robot_y = col, row
    
    for instruction in instructions:
        robot_x, robot_y = parse_instructions(grid, instruction, robot_x, robot_y)

    # Calculate coordinates
    sum = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'O':
                sum += (100 * row + col)
    print(sum)
    pass

def replace_tile(grid, x, y, new_x, new_y, tile='@'):
    grid[new_y][new_x] = tile
    grid[y][x] = '.'
    pass

def find_neighbor_boxes(y, x, dx, dy, grid):
    if grid[y + dy][x] == "[":
        return (y + dy, x), (y + dy, x + 1)
    return (y + dy, x - 1), (y + dy, x)

def move_box_part_two(grid, x, y, dx, dy):
    """
    Inspired by solution posted by Sensitive-Sink-8230
    See here: https://github.com/fivard/AOC-2024/blob/master/day15/star2.py
    """
    if dy == 0: # Moving horizontally?
        new_x, new_y = x + dx, y + dy
        while grid[new_y][new_x] in ['[', ']']: # Iterate past adjacent boxes
            new_x, new_y = new_x + dx, new_y + dy
        if grid[new_y][new_x] == '#': # No empty space
            return False
        while (new_y, new_x) != (y, x):
            new_y, new_x = new_y - dy, new_x - dx
            replace_tile(grid, new_x, new_y, new_x + dx, new_y + dy, grid[new_y][new_x])
        return True

    # Otherwise moving vertically (dy != 0)
    neighbors = [find_neighbor_boxes(y, x, dx, dy, grid)] # Look for neighbors above box

    i = 0
    while i < len(neighbors): # Gather all vertical neighbors of box
        neighbor = neighbors[i]
        left, right = neighbor[0], neighbor[1]
        new_y_left, new_x_left = left[0] + dy, left[1] + dx
        new_y_right, new_x_right = right[0] + dy, right[1] + dx

        if grid[new_y_left][new_x_left] == '#' or grid[new_y_right][new_x_right] == '#':
            return False
        if grid[new_y_left][new_x_left] in ['[' , ']']:
            neighbors.append(find_neighbor_boxes(left[0], left[1], dx, dy, grid))
        if grid[new_y_right][new_x_right] == '[':
            neighbors.append(find_neighbor_boxes(right[0], right[1], dx, dy, grid))
        i += 1

    i -= 1
    while i >= 0: # Swap neighbors away from robot
        neighbor = neighbors[i]
        left, right = neighbor[0], neighbor[1]
        replace_tile(grid, left[1],  left[0],  left[1] + dx,  left[0] + dy,  '[')
        replace_tile(grid, right[1], right[0], right[1] + dx, right[0] + dy, ']')
        i -= 1
    return True

def parse_instructions_part_two(grid, instruction, robot_x, robot_y):
    dy, dx = velocity[instruction]
    if grid[robot_y + dy][robot_x + dx] == '#': # Wall in new position
        return robot_x, robot_y
    if grid[robot_y + dy][robot_x + dx] in ['[', ']']: # Box in new position
        if move_box_part_two(grid, robot_x, robot_y, dx, dy):
            replace_tile(grid, robot_x, robot_y, robot_x + dx, robot_y + dy, '@')
            return robot_x + dx, robot_y + dy
        return robot_x, robot_y

    # Not a wall or box
    replace_tile(grid, robot_x, robot_y, robot_x + dx, robot_y + dy, '@')
    return robot_x + dx, robot_y + dy

def solve_part_two(): # 'large' example is 9021
    input = parse_input("day15.txt")
    grid, instructions = ''.join(input).split("\n\n")
    grid = [[col for col in row.strip('\n')] for row in grid.split('\n')]
    instructions = [str(instruction) for instruction in instructions.replace('\n', "")]
    
    # Expand boxes to increase size
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'O':
                grid[row][col] = '[]'
            elif grid[row][col] == '#':
                grid[row][col] = '##'
            elif grid[row][col] == '.':
                grid[row][col] = ".."
            elif grid[row][col] == '@':
                grid[row][col] = '@.'

    grid = [[x for x in ''.join(row)] for row in grid]

    # Find robot start position
    robot_x, robot_y = -1, -1
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                robot_x, robot_y = col, row

    # Process instructions
    for instruction in instructions:
        robot_x, robot_y = parse_instructions_part_two(grid, instruction, robot_x, robot_y)

    # Calculate coordinates
    print(sum([100 * i + j if grid[i][j] == '[' else 0 for i in range(len(grid)) for j in range(len(grid[i]))]))

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))

