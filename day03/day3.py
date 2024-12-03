from functools import reduce
import re
import timeit

def parse_input(filename):
    return open(filename, 'r').read()

def product(list):
    product = 1
    for elem in list:
        product *= elem
    return product

def solve_part_one():    
    print(sum([reduce(lambda x, y: x * y, [int(i) for i in instruction.strip("mul()").split(",")]) for instruction in re.findall("mul\(\d{1,3},\d{1,3}\)", open("day03.txt", 'r').read())]))

def solve_part_two():
    sum = 0
    mul = True
    input = parse_input("day03.txt")
    instructions = re.findall("(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", input)
    for instruction in instructions:
        if instruction == "don't()":
           mul = False
        elif instruction == "do()":
           mul = True
        else:
            if mul:
                sum += product([int(i) for i in instruction.strip("mul()").split(",")])
    print(sum)
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))