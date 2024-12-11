import timeit

def parse_input(filename):
    return [[x for x in y] for y in open(filename, 'r')]

def get_index(input, row, col):
    if row < 0 or row > len(input) - 1:
        return ""
    if col < 0 or col > len(input) - 1:
        return ""
    return input[row][col]

def solve_part_one():
    pass

def solve_part_two():
    antinodes = set()
    input = parse_input("day08.txt")

    for row in range(len(input)):
        for col in range(len(input[0])):
            if input[row][col] != '.': # Non-empty cell
                for i in range(1, len(input)):
                    for j in range(1, len(input)):
                        if get_index(input, row + i, col + j) == input[row][col]:
                            k = 0
                            while get_index(input, row + (k*i), col + (k*j)) != "":
                                antinodes.add((row + (k*i), col + (k*j)))
                                k += 1
                        if get_index(input, row - i, col - j) == input[row][col]:
                            k = 0
                            while get_index(input, row - (k*i), col - (k*j)) != "":
                                antinodes.add((row - (k*i), col - (k*j)))
                                k += 1
                        if get_index(input, row + i, col - j) == input[row][col]:
                            k = 0
                            while get_index(input, row + (k*i), col - (k*j)) != "":
                                antinodes.add((row + (k*i), col - (k*j)))
                                k += 1
                        if get_index(input, row - i, col + j) == input[row][col]:
                            k = 0
                            while get_index(input, row - (k*i), col + (k*j)) != "":
                                antinodes.add((row - (k*i), col + (k*j)))
                                k += 1
    print(len(antinodes))

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
