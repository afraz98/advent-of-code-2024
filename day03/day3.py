import re

def parse_input(filename):
    return open(filename, 'r').read()

def product(list):
    product = 1
    for elem in list:
        product *= elem
    return product

def solve_part_one():
    summ = 0
    input = parse_input("day03.txt")
    instructions = re.findall("mul\(\d{1,3},\d{1,3}\)", input)
    for instruction in instructions:
       summ += product([int(i) for i in instruction.strip("mul()").split(",")])
    print(summ)
    pass

def solve_part_two():
    pass

solve_part_one()
solve_part_two()