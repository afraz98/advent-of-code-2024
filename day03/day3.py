from functools import reduce
import re

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

solve_part_one()
solve_part_two()