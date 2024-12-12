def parse_input(filename):
    return [[x for x in y] for y in open(filename, 'r')]

def adj(x, y, crop, shape, input):
    if x < 0 or x > len(input): # Invalid position
        return shape
    if y < 0 or y > len(input): # Invalid position
        return shape
    if input[y][x] != crop: # Different crop planted
        return shape

    pass

def solve_part_one():
    input = parse_input("day12_test.txt")
    print(adj(0,0,input[0][0], [], input))
    pass

def solve_part_two():
    pass

