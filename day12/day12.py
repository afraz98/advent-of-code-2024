import timeit

def parse_input(filename):
    return [[x for x in y.strip()] for y in open(filename, 'r')]

def adj(x, y, crop, shape, field, visited):
    if x < 0 or x > len(field)-1: # Invalid position
        return shape

    if y < 0 or y > len(field[0])-1: # Invalid position
        return shape

    if field[y][x] != crop: # Different crop planted
        return shape
    
    if visited[y][x]: # Position already visited
        return shape
    visited[y][x] = True

    shape.add((x,y))
    return adj(x+1, y, crop, shape, field, visited) | adj(x, y+1, crop, shape, field, visited) | adj(x-1, y, crop, shape, field, visited) | adj(x, y-1, crop, shape, field, visited)

def perimeter(shape, crop, field):
    perimeter = 0
    for cell in shape:
        col, row = cell[0], cell[1]
        if row + 1 >= len(field) or field[row+1][col] != crop:
            perimeter += 1
        if row - 1 < 0 or field[row-1][col] != crop:
            perimeter += 1
        if col + 1 >= len(field) or field[row][col+1] != crop:
            perimeter += 1
        if col - 1 < 0 or field[row][col-1] != crop:
            perimeter += 1
    return perimeter

def solve_part_one():
    field = parse_input("day12.txt")
    sum = 0

    visited = [[False for _ in row] for row in field]
    for row in range(0, len(field)):
        for col in range(0, len(field[0])):
            shape = adj(col, row, field[row][col], set(), field, visited)
            if len(shape) > 0:
                sum += (len(shape) * perimeter(shape, field[row][col], field))
    print(sum)

def solve_part_two():
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))    
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
