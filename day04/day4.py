# Need to traverse word search forward, backwards, up, down, and diagonally to determine 
# where 'XMAS' is.

import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def test_coordinates(a,b,c,d, word_search):
    count = 0
    if(word_search[a[0]][a[1]] + word_search[b[0]][b[1]] + word_search[c[0]][c[1]] + word_search[d[0]][d[1]] == 'XMAS' and all([x >= 0 for x in [a[0], a[1], b[0], b[1], c[0], c[1], d[0], d[1]]])):
        count += 1
    if(word_search[a[0]][a[1]] + word_search[b[0]][b[1]] + word_search[c[0]][c[1]] + word_search[d[0]][d[1]] == 'SAMX' and all([x >= 0 for x in [a[0], a[1], b[0], b[1], c[0], c[1], d[0], d[1]]])):
        count += 1
    return count

def solve_part_one():
    word_search = [list(x) for x in parse_input("day04.txt")] # Column-major
    count = 0

    # Traverse list horizontally
    for col in range(0, len(word_search[0])):
        for row in range(0, len(word_search)):
            try:
                count += test_coordinates((col, row), (col + 1, row), (col + 2, row), (col+3, row), word_search)
            except:
                pass

    # Traverse list vertically
    for col in range(0, len(word_search[0])):
        for row in range(0, len(word_search)):
                try:
                    count += test_coordinates((col, row), (col, row + 1), (col, row + 2), (col, row + 3), word_search)  
                except:
                    pass

    # Traverse list diagonally (left-to-right)
    for col in range(0, len(word_search[0])):
        for row in range(0, len(word_search)):
                try:
                    count += test_coordinates((col, row), (col + 1, row + 1), (col + 2, row + 2), (col + 3, row + 3), word_search)  
                except:
                    pass

    # Traverse list diagonally (right-to-left)
    for col in range(0, len(word_search[0])):
        for row in range(0, len(word_search)):
            try:
                count += test_coordinates((col, row), (col + 1, row - 1), (col + 2, row - 2), (col + 3, row - 3), word_search)  
            except:
                pass

    print(count)
    pass

def find_mas_x(word_search, row, col):
    if row + 1 >= len(word_search) or row - 1 < 0:
        return 0
    
    if col + 1 >= len(word_search) or col - 1 < 0:
        return 0

    if word_search[col - 1][row - 1] == 'M' and word_search[col + 1][row + 1] == 'S':
        if word_search[col - 1][row + 1] == 'M' and word_search[col + 1][row - 1] == 'S':
            return 1
        if word_search[col - 1][row + 1] == 'S' and word_search[col + 1][row - 1] == 'M':
            return 1

    if word_search[col - 1][row - 1] == 'S' and word_search[col + 1][row + 1] == 'M':
        if word_search[col - 1][row + 1] == 'M' and word_search[col + 1][row - 1] == 'S':
            return 1
        if word_search[col - 1][row + 1] == 'S' and word_search[col + 1][row - 1] == 'M':
            return 1

def solve_part_two():
    word_search = [list(x) for x in parse_input("day04.txt")] # Column-major
    count = 0

    # Traverse list horizontally
    for col in range(0, len(word_search[0])):
        for row in range(0, len(word_search)):
            try:
                if(word_search[col][row] == 'A'):
                    count += find_mas_x(word_search, row, col)
            except:
                pass
    print(count)
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))