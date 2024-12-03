import re

def product(list):
    product = 1
    for elem in list:
        product *= elem
    return product

def solve_part_one():    
    print(sum([product([int(i) for i in instruction.strip("mul()").split(",")]) for instruction in re.findall("mul\(\d{1,3},\d{1,3}\)", open("day03.txt", 'r').read())]))

def solve_part_two():
    pass

solve_part_one()
solve_part_two()