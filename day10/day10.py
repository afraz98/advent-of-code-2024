import timeit, sys

def print_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            print(grid[row][col], end='')
        print()

def parse_input(filename):
    return [[x for x in y.strip()] for y in open(filename, 'r')]

# Recursive breadth-first search for peaks
def find_trails(set, row, col, map, visited, last_value):
    if row < 0 or row > len(map) - 1: # Row out of bounds
        return set
    
    if col < 0 or col > len(map) - 1: # Column out of bounds
        return set
    
    if visited[row][col]: # Node already visited
        return set  

    if int(map[row][col]) != last_value + 1: # Too steep / decline
        return set

    if int(map[row][col]) == 9: # Reached peak
        set.add((row, col))
        return set
    
    return find_trails(set, row, col+1, map, visited, int(map[row][col]))  | \
            find_trails(set, row+1, col, map, visited, int(map[row][col])) |  \
            find_trails(set, row-1, col, map, visited, int(map[row][col])) | \
            find_trails(set, row, col-1, map, visited, int(map[row][col]))

# Managed to stumble across this solution while solving part one :-)
def find_trails_part_two(row, col, map, visited, last_value):
    if row < 0 or row > len(map) - 1: # Row out of bounds
        return 0
    
    if col < 0 or col > len(map) - 1: # Column out of bounds
        return 0
    
    if visited[row][col]: # Node already visited
        return 0    
    
    if int(map[row][col]) != last_value + 1: # Too steep / decline
        return 0

    if int(map[row][col]) == 9: # Reached peak
        return 1

    return find_trails_part_two(row + 1, col, map, visited, int(map[row][col])) + \
        find_trails_part_two(row, col + 1, map, visited, int(map[row][col])) + \
        find_trails_part_two(row - 1, col, map, visited, int(map[row][col])) + \
        find_trails_part_two(row, col - 1, map, visited, int(map[row][col]))

def solve_part_one(): # test input should be 36
    map = parse_input("day10.txt")
    trail_heads = [(row_index,col_index) for row_index, row in enumerate(map) 
                   for col_index, element in enumerate(row) if element == '0']
        
    # Find paths for each trail head
    print(sum([len(find_trails(set(), trail_head[0], trail_head[1], map, [[False for _ in row] for row in map], -1)) for trail_head in trail_heads]))
    
def solve_part_two():
    map = parse_input("day10.txt")
    trail_heads = [(row_index,col_index) for row_index, row in enumerate(map) 
                   for col_index, element in enumerate(row) if element == '0']
    # Find paths for each trail head
    print(sum([find_trails_part_two(trail_head[0], trail_head[1], map, [[False for _ in row] for row in map], -1) for trail_head in trail_heads]))

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))    
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
