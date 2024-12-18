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
    input = parse_input("day15_test2.txt")
    grid, instructions = ''.join(input).split("\n\n")
    grid = [[col for col in row.strip('\n')] for row in grid.split('\n')]

    instructions = [str(instruction) for instruction in instructions.replace('\n', "")]
    print(instructions)

    robot_x, robot_y = -1, -1
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                robot_x, robot_y = col, row
    
    for instruction in instructions:
        print("Move %s" % instruction)
        robot_x, robot_y = parse_instructions(grid, instruction, robot_x, robot_y)
        print_grid(grid)
    pass

def solve_part_two():
    input = parse_input("day15_test.txt")
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))

