import timeit
from functools import lru_cache

def parse_input(filename):
    return [[x.strip("\r\n") for x in line.split(" ")] for line in open(filename, 'r')][0]

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0: # Even number of digits
            new_stones.append(str(int(stone[:(len(stone) // 2)])))
            new_stones.append(str(int(stone[(len(stone) // 2):])))
        else:
            new_stones.append(str(int(stone) * 2024))
    return new_stones

def solve_part_one():
    stones = parse_input("day11.txt")
    print(stones)
    for _ in range(25):
        stones = blink(stones)
    print(len(stones))
    pass

# Iterative approach is too slow for 75 "blinks" -- 
# See if there are patterns that can be evaluated without traversing through new stones?
@lru_cache
def solve_part_two():
    stones = parse_input("day11.txt")
    print(stones)
    for x in range(50):
        stones = blink(stones)
        print(x)
    print(len(stones))
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
