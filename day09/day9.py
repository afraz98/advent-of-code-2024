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

# Move each block individually
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

def expand_input_part_two(input):
    expanded = []
    id = 0
    for i in range(len(input)):
        if i % 2 == 0:
            expanded.append([str(id) for _ in range(int(input[i]))])
            id = id + 1
        else:
            expanded.append(["." for _ in range(int(input[i]))])
    return expanded

def print_disk(disk):
    for entry in disk:
        print(''.join(entry), end='')
    print()

# Move files (blocks of same ID) together
def solve_part_two():
    disk = expand_input_part_two(parse_input("day9_test.txt"))
    print_disk(disk)
    j = len(disk) - 1
    
    while j > 0 and disk[j][0] != 0:
        swap = False
        for i in range(len(disk)):
            print(disk[j], disk[i])
            if j <= i:
                break
            if len(disk[j]) > len(disk[i]):
                continue
            while not swap and j > i and disk[i][0] == '.':
                print("swap")
                if disk[j][0] !=  ".":
                    if len(disk[j]) == len(disk[i]): # Swap entire block
                        disk[j], disk[i] = disk[i], disk[j]
                        print_disk(disk)
                        swap = True
                    if len(disk[j]) < len(disk[i]): # Split into two regions
                        for idx in range(len(disk[j])):
                            disk[j][idx], disk[i][idx] = disk[i][idx], disk[j][idx]
                        print_disk(disk)
                        swap = True
                j -= 1
        print_disk(disk)
        j -= 1
    print_disk(disk)
    print(sum([i * len(disk[i]) if disk[i][0] != '.' else 0 for i in range(len(disk))])) # Calculate checksum
    pass

# result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
# print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
