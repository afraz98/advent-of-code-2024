import copy
import timeit

direction_print = ['^', '>', 'v', '<']
dx_dy = [(0, -1), (1,0), (0, 1), (-1, 0)]

def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid)):
            print(grid[y][x], end='')
        print()

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def find_new_coordinates(x, y, direction):
    dx, dy = dx_dy[direction]
    return x+dx, y+dy

def peek(x, y, input):
    if 0 <= x < len(input) and 0 <= y < len(input):
        if(input[y][x] == '#'):
            return False
    return True

def find_coordinates(start_x, start_y, grid):
    direction = 0
    tiles = 0

    x = start_x
    y = start_y
    while 0 <= x < len(grid[0]) - 1 and 0 <= y < len(grid) - 1:
        new_x, new_y = find_new_coordinates(x, y, direction)
        if not peek(new_x, new_y, grid):
            direction = (direction + 1) % 4
            new_x, new_y = find_new_coordinates(x, y, direction)
        x = new_x
        y = new_y
        grid[y][x] = direction_print[direction]

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] in direction_print:
                tiles += 1
    return tiles

def find_coordinates_part_two(start_x, start_y, grid):
    direction = 0
    steps_taken = 0

    x = start_x
    y = start_y

    while 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        steps_taken += 1
        if steps_taken > len(grid) * len(grid[0]):
            return -1
        new_x, new_y = find_new_coordinates(x, y, direction)
        if not peek(new_x, new_y, grid):
            direction = (direction + 1) % 4
            new_x, new_y = find_new_coordinates(x, y, direction)
        x = new_x
        y = new_y
    return 0

def solve_part_one():
    start_x, start_y = 0, 0
    grid = [[x for x in y] for y in parse_input("day06.txt")]

    # Find starting position
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '^':
                start_x, start_y = x, y
    print(find_coordinates(start_x, start_y, grid))

def solve_part_two():
    invalid = 0
    start_x, start_y = 0, 0
    grid = [[x for x in y] for y in parse_input("day06.txt")]

    # Find starting position
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '^':
                start_x, start_y = x, y

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if x == start_x and y == start_y:
                continue
            temp = copy.deepcopy(grid)
            temp[y][x] = '#'
            if find_coordinates_part_two(start_x, start_y, temp) == -1:
                invalid += 1
    print(invalid)

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))