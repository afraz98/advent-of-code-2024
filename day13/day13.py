import timeit
import re

def parse_input(filename):
    return [block.split('\n') for block in open(filename, 'r').read().split("\n\n")]

"""
    Cramer's Rule for a 2x2 matrix representing
    A system of equations similar to the following:
    {A B}{x} = {P_x}
    {A B}{y} = {P_x}
"""
def cramer(a_x, b_x, a_y, b_y, p_x, p_y):
    return ((p_x * b_y) - (p_y * b_x)) / (a_x * b_y - (a_y * b_x)), ((a_x * p_y) - (a_y * p_x)) / (a_x * b_y - (a_y * b_x))


def solve_part_one():
    tokens = 0
    entries = parse_input("day13.txt") 
    for entry in entries:
        button_a = [int(number) for number in re.findall(r"\d+", entry[0])]
        button_b = [int(number) for number in re.findall(r"\d+", entry[1])]
        prize = [int(number) for number in re.findall(r"\d+", entry[2])]
        A,B = cramer(button_a[0], button_b[0], button_a[1], button_b[1], prize[0], prize[1])
        if 0 <= A < 100 and 0 <= B < 100:
            if round(A) == A and round(B) == B:
                tokens += 3*A + B
    print(int(tokens))

# Cramer's rule
def solve_part_two():
    tokens = 0
    entries = parse_input("day13.txt") 
    for entry in entries:
        button_a = [int(number) for number in re.findall(r"\d+", entry[0])]
        button_b = [int(number) for number in re.findall(r"\d+", entry[1])]
        prize = [10000000000000 + int(number) for number in re.findall(r"\d+", entry[2])]
        A,B = cramer(button_a[0], button_b[0], button_a[1], button_b[1], prize[0], prize[1])
        if round(A) == A and round(B) == B:
            tokens += 3*A + B
    print(tokens)

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))    
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
