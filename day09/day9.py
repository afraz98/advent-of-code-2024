import timeit

def parse_input(filename):
    return open(filename).read().strip("\r\n")

def calculate_checksum(disk):
    return sum([i * int(v) if disk[i] != '.' else 0 for i,v in enumerate(disk)])

def expand_input(input): # Why is there an empty list between some of the elements?
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
    return list(filter(lambda x: x != [], expanded))

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
            if int(input[i]) != 0:
                for _ in range(int(input[i])):
                    expanded.append(id)
            id = id + 1
        else: # Empty space
            if int(input[i]) != 0:
                for _ in range(int(input[i])):
                    expanded.append(-1)
    return id, expanded

def print_disk(disk):
    for entry in disk:
        print(','.join(str(entry)), end='')
    print()

def defragment_disk(max_id, disk):
    end_id = len(disk) - 1
    id = max_id - 1
    while id >= 0:
        # Look for ID region
        while disk[end_id] != id: # Find end index (iterating from end of list)
            end_id -= 1

        start_id = end_id - 1
        while disk[start_id] == id: # Find starting index
            start_id -= 1
        id_size = end_id - start_id

        # Look for empty region
        start_empty = 0
        while start_empty < start_id:
            while disk[start_empty] != -1: # Find starting index of empty region
                start_empty = start_empty + 1

            end_empty = start_empty
            while disk[end_empty] == -1: # Find end index of empty region
                end_empty += 1
            empty_size = end_empty - start_empty

            if empty_size >= id_size: # Empty region of adequate size found
                break
            start_empty += empty_size # Otherwise continue iterating 

        # Swap ID, empty region
        if empty_size >= id_size and start_id > start_empty:
            for i in range(0, id_size):
                disk[start_empty + i] = id

            for j in range(0, id_size):
                disk[end_id - j] = -1
        id = id - 1
    return disk

def solve_part_two(): # Move files (blocks of same ID) together
    id, disk = expand_input_part_two(parse_input("day9.txt")) # Example should be 2858
    disk = defragment_disk(id, disk)

    disk_str = ""
    for i in range(len(disk)):
        if disk[i] == -1:
            disk[i] = 0

    print(sum([i * v for i, v in enumerate(disk)]))
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
