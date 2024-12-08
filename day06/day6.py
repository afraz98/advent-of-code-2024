import timeit

def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid)):
            print(grid[y][x], end='')
        print()

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def find_new_coordinates(x, y, direction):
    new_x = 0
    new_y = 0

    if direction == 0: # up
        new_x = x
        new_y = y - 1
    if direction == 1: # right
        new_x = x + 1
        new_y = y
    if direction == 2: # down
        new_x = x
        new_y = y + 1
    if direction == 3: # left
        new_x = x - 1
        new_y = y
    return new_x, new_y    

def peek(x,y,input,direction):
    if 0 <= x < len(input) and 0 <= y < len(input):
        if(input[y][x] == '#'):
            return False
    return True

def solve_part_one():
    tiles = 0
    start_x, start_y = 0, 0
    input = [[x for x in y] for y in parse_input("day06.txt")]
    direction = 0

    # Find starting position
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == '^':
                start_x, start_y = x,y

    x = start_x
    y = start_y

    while 0 <= x < len(input[0]) - 1 and 0 <= y < len(input) - 1:
        newx, newy = find_new_coordinates(x, y, direction)
        if not peek(newx, newy, input, direction):
            direction = (direction + 1) % 4
            newx, newy = find_new_coordinates(x, y, direction)
        x = newx
        y = newy
        input[y][x] = 'X'

    for y in range(0, len(input)):
        for x in range(0, len(input[0])):
            if input[y][x] == 'X':
                tiles += 1
    print(tiles)

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))