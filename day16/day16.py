import timeit

def parse_input(filename):
    return [[x for x in row] for row in open(filename, 'r')]

# Probably need to implement A* as with previous years.
def solve_part_one():
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
