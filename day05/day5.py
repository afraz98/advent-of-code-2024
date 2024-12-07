import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def test_rule(order, rule):
    before, after = rule.split("|")

    if not int(before) in order:
        return True

    if not int(after) in order:
        return True
    
    return order.index(int(before)) < order.index(int(after))
    pass

def test_order(order, rules):
    return all([test_rule(order, rule) for rule in rules])

def solve_part_one():
    count = 0
    input = parse_input("day05.txt")

    rules = input[:input.index('')]
    orders = [[int(y) for y in x.split(",")] for x in input[input.index('') + 1:]]

    for order in orders:
        count += order[len(order) // 2] if test_order(order, rules) else 0

    print(count)
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))