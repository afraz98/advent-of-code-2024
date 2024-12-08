import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def solve_part_one():
    input = parse_input("day07_test.txt")
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))