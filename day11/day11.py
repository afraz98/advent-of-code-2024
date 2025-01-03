import timeit

"""
Leverage memoization to avoid re-processing nodes we have already visited for a 
given blink iteration. The result of each stone is stored in a dictionary as follows:

(stone, iteration) -> (result length)

Inspired by solution posted by u/skumonti
"""

def parse_input(filename):
    return [[int(x.strip("\r\n")) for x in line.split(" ")] for line in open(filename, 'r')][0]

def blink(stone, i, memo={}):
    if i == 0:
        return 1
    if (stone, i) in memo:
        return memo[(stone,i)]

    if stone == 0:
        val = blink(1, i-1, memo)
    elif len(str(stone)) % 2 == 0: # Even number of digits
        stg = str(stone)
        val = blink(int(str(stg[(len(stg) // 2):])), i-1, memo) + blink(int(str(stg[:(len(str(stg)) // 2)])), i-1, memo)
    else: # Odd number of digits
        val = blink(stone * 2024, i - 1, memo)

    memo[(stone,i)] = val
    return val

def solve_part_one():
    memo = {}
    print(sum([blink(stone, 25, memo) for stone in parse_input("day11.txt")]))

def solve_part_two():
    memo = {}
    print(sum([blink(stone, 75, memo) for stone in parse_input("day11.txt")]))

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
