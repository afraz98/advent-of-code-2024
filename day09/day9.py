import timeit

def parse_input(filename):
    return open(filename).read().strip("\r\n")

def expand_input(input):
    id = 0
    expanded = []
    for i in range(0, len(input)):
        if i % 2 == 0:
            for _ in range(int(input[i])):
                expanded.append(str(id))
            id = id + 1
        else:
            for _ in range(int(input[i])):
                expanded.append(".")
    return expanded

# FIXME: Don't think I'm accounting for multi-character IDs...
def solve_part_one():
    disk = expand_input(parse_input("day9.txt"))        
    j = len(disk) - 1
    for i in range(len(disk)):
        if j <= i:
            break
        while disk[i] == "." and j > i:
            if disk[j] !=  ".":
                disk[j], disk[i] = disk[i], disk[j] # Swap spaces
                j -= 1
                break
            j -= 1
    print(sum([i * int(disk[i]) if disk[i] != '.' else 0 for i in range(len(disk))])) # Calculate checksum

def solve_part_two():
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
