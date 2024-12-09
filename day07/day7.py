import timeit
from itertools import product, zip_longest, combinations

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]


def solve_part_one():
    total = 0
    input = parse_input("day07_test.txt")
    for line in input:
        lvalue, rvalue = line.split(":")
        rvalue = [int(i) for i in rvalue.split(" ")[1:]]
        operators = [list(x) for x in product(['+', '*'], repeat=len(rvalue)-1)] # from here: https://github.com/RD-Dev-29/advent_of_code_24/blob/main/code_files/day7.py
        for operator in operators:
            sequences = [item for pair in zip_longest(rvalue, operator) for item in pair if item is not None]
            print(sequences)
    print(total)
    pass

def solve_part_two():
    input = parse_input("day07_test.txt")
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))