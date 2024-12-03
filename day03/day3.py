from functools import reduce
import re

def solve_part_one():    
    print(sum([reduce(lambda x, y: x * y, [int(i) for i in instruction.strip("mul()").split(",")]) for instruction in re.findall("mul\(\d{1,3},\d{1,3}\)", open("day03.txt", 'r').read())]))

def solve_part_two():
    pass

solve_part_one()
solve_part_two()