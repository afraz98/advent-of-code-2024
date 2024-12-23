import timeit

def parse_input(filename):
    return open(filename).read().strip("\r\n")

def calculate_checksum(disk):
    return sum([i * int(disk[i]) if disk[i] != '.' else 0 for i in range(len(disk))])

def expand_input(input):
    id = 0
    expanded = []
    for i in range(0, len(input)):
        if input[i] == 0:
            id = id + 1
        elif i % 2 == 0:
            for _ in range(int(input[i])):
                expanded.append(str(id))
            id = id + 1
        else:
            for _ in range(int(input[i])):
                expanded.append(".")
    return expanded

def solve_part_one(): # Move each block individually
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
    print(calculate_checksum(disk)) # Calculate checksum

def expand_input_part_two(input):
    expanded = []
    id = 0
    for i in range(len(input)):
        if i % 2 == 0:
            if(int(input[i]) != 0):
                expanded.append([str(id) for _ in range(int(input[i]))])
            id = id + 1
        else:
            if (int(input[i] != 0)):
                expanded.append(["." for _ in range(int(input[i]))])
    return expanded

def print_disk(disk):
    for entry in disk:
        print(''.join(entry), end='')
    print()

def move_files(disk, i, j):
    if len(disk[j]) == len(disk[i]) and disk[i].count('.') >= len(disk[j]): # Swap entire block
        disk[j], disk[i] = disk[i], disk[j]
        return True
    if len(disk[j]) < len(disk[i]) and disk[i].count('.') >= len(disk[j]): # Swap blocks element-wise
        for idx in range(len(disk[j])):
            disk[j][idx], disk[i][disk[i].index('.')] = disk[i][disk[i].index('.')], disk[j][idx]
        return True
    return False

def defragment_disk(disk):
    j = len(disk) - 1
    while j > 0:
        i = 0
        while j > i and not move_files(disk, i, j):
            i += 1
        j -= 1
    return disk

def solve_part_two(): # Move files (blocks of same ID) together
    disk = expand_input_part_two(parse_input("day9.txt"))
    disk = defragment_disk(disk)

    disk_str = ""
    for i in range(len(disk)):
        disk_str += ''.join([x for x in disk[i]])
    print(calculate_checksum(disk_str)) # Calculate checksum
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
