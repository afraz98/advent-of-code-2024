from itertools import permutations
import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def solve_part_one():
    sum = 0

    input = parse_input("day19_test.txt")
    towels = input[0].replace(" ", "").split(",")
    patterns = input[2:]

    towels.sort(key=lambda x: len(x), reverse=True) # Sort towels by pattern length
    for pattern in patterns: # Use regular expressions to extract each towel until pattern is empty?
        used_towels = []
        print("%s " % pattern, end='')
        for towel in towels:
            if towel in pattern:
                pattern = pattern.replace(towel, "")
                used_towels.append(towel)
        print("%s " % used_towels, end='')
        print("%s " % pattern)
        if len(pattern) == 0:
            sum += 1

    print(sum)
    pass

def solve_part_two():
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
