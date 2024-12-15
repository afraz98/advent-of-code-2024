import timeit
import re
import numpy as np # Work smart, not hard

def parse_input(filename):
    return [block.split('\n') for block in open(filename, 'r').read().split("\n\n")]

"""
 Pick button presses such that the prize is won minimizing tokens spent.
 Each input block is a system of equations that can be solved with matrix operations.
 Solve for A,B where each variable in the number of times a button is pressed:
 
 { X1  X1} {A} = { X }
 { Y1  Y2} {B} = { Y }
"""
def find_combination(button_A, button_B, prize):
    sln = np.linalg.lstsq(np.array(list(zip(button_A, button_B))),np.array(prize))
    print(sln[0])
    return 3*sln[0][0] + sln[0][1]

def solve_part_one():
    tokens = 0
    entries = parse_input("day13.txt") 
    for entry in entries:
        button_a = [int(number) for number in re.findall(r"\d+", entry[0])]
        button_b = [int(number) for number in re.findall(r"\d+", entry[1])]
        prize = [int(number) for number in re.findall(r"\d+", entry[2])]
#        tokens += find_combination(button_a, button_b, prize)
        for i in range(100):
            for j in range(100):
                if i*button_a[0] + j*button_b[0] == prize[0] and i*button_a[1] + j*button_b[1] == prize[1]:
                    tokens += (3*i + j)
    print(tokens)

def solve_part_two():
    pass

solve_part_one()