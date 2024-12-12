def parse_input(filename):
    return open(filename).read().strip("\r\n")

def expand_input(input):
    id = 0
    expanded = ""
    for i in range(0, len(input)):
        if i % 2 == 0:
            expanded += str(id) * int(input[i])
            id += 1
        else:
            expanded += "." * int(input[i])
    return expanded
def solve_part_one():
    print(expand_input(parse_input("day9_test.txt")))
    pass

def solve_part_two():
    pass

solve_part_one()