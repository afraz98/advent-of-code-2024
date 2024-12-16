import re, timeit, os

import matplotlib.pyplot as plt
import numpy as np

def print_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            print(grid[row][col], end='')
        print()

def parse_input(filename):
    return [line for line in open(filename, 'r')]

def solve_test_input():
    safety_score = 1
    width = 11
    height = 7
    grid = [[0 for _ in range(width)] for _ in range(height)]
    robots = [[int(number) for number in re.findall(r'[-+]?\d*\.?\d+', line)] for line in parse_input("day14_test.txt")]
    for _ in range(100):
        for robot in robots:
            robot[0] = (robot[0] + robot[2]) % width
            robot[1] = (robot[1] + robot[3]) % height
        pass
    
    for robot in robots:
        grid[robot[1]][robot[0]] += 1
    
    # Calculate safety score for each quadrant
    quadrant_score = 0
    for row in range(0, height // 2):
        for col in range(0, width // 2):
            if(grid[row][col] != "."):
                quadrant_score += int(grid[row][col])
    print(quadrant_score)
    safety_score *= quadrant_score

    quadrant_score = 0
    for row in range(0, height // 2):
        for col in range(width // 2 + 1, width):
            if(grid[row][col] != "."):
                quadrant_score += int(grid[row][col])
    print(quadrant_score)
    safety_score *= quadrant_score

    quadrant_score = 0
    for row in range(height // 2 + 1, height):
        for col in range(0, width // 2):
            if(grid[row][col] != "."):
                quadrant_score += int(grid[row][col])
    print(quadrant_score)
    safety_score *= quadrant_score

    quadrant_score = 0
    for row in range(height // 2 + 1, height):
        for col in range(width // 2 + 1, width):
            if(grid[row][col] != "."):
                quadrant_score += int(grid[row][col])
    print(quadrant_score)
    safety_score *= quadrant_score

    print(safety_score)
    pass

def calculate_safety_score(grid, height, width):
    safety_score = 1
    # Calculate safety score for each quadrant
    quadrant_score = 0
    for row in range(0, height // 2):
        for col in range(0, width // 2):
            if(grid[row][col] != "."):
                quadrant_score += int(grid[row][col])
    safety_score *= quadrant_score

    quadrant_score = 0
    for row in range(0, height // 2):
        for col in range(width // 2 + 1, width):
            if(grid[row][col] != "."):
                quadrant_score += int(grid[row][col])
    safety_score *= quadrant_score

    quadrant_score = 0
    for row in range(height // 2 + 1, height):
        for col in range(0, width // 2):
            if(grid[row][col] != "."):
                quadrant_score += int(grid[row][col])
    safety_score *= quadrant_score

    quadrant_score = 0
    for row in range(height // 2 + 1, height):
        for col in range(width // 2 + 1, width):
            if(grid[row][col] != "."):
                quadrant_score += int(grid[row][col])
    safety_score *= quadrant_score
    return safety_score

def solve_part_one():
    width = 101
    height = 103
    grid = [[0 for _ in range(width)] for _ in range(height)]
    robots = [[int(number) for number in re.findall(r'[-+]?\d*\.?\d+', line)] for line in parse_input("day14.txt")]
    
    for _ in range(100):
        for robot in robots:
            robot[0] = (robot[0] + robot[2]) % width
            robot[1] = (robot[1] + robot[3]) % height
        pass

    for robot in robots:
        grid[robot[1]][robot[0]] += 1

    print(calculate_safety_score(grid,height,width))
    pass

def find_square(matrix, size):
  """Finds a square of 1s of the given size in a 2D array.

  Args:
    matrix: The 2D array to search.
    size: The size of the square to find.

  Returns:
    The coordinates of the top-left corner of the square, or None if no such 
    square exists.
  """

  rows = len(matrix)
  cols = len(matrix[0])

  for i in range(rows - size + 1):
    for j in range(cols - size + 1):
      if all(matrix[i + x][j + y] != 0 for x in range(size) for y in range(size)):
        return i, j

  return None

def find_line(grid, n):
    """Finds lines of length n of the same character in a 2D array.

    Args:
        array (list): The 2D array to search.
        n (int): The length of the line to find.
        char (str): The character to search for.

    Returns:
        list: A list of tuples, where each tuple contains the starting coordinates and direction of the line.
    """

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols - n + 1):
            if all(grid[i][j + k] != 0 for k in range(n)):
                return True

    for i in range(rows - n + 1):
        for j in range(cols):
            if all(grid[i + k][j] != 0 for k in range(n)):
                return True
    return False

def solve_part_two():
    width = 101
    height = 103
    grid = [[0 for _ in range(width)] for _ in range(height)]
    robots = [[int(number) for number in re.findall(r'[-+]?\d*\.?\d+', line)] for line in parse_input("day14.txt")]

    for iteration in range(10000):
        grid = [[0 for _ in range(width)] for _ in range(height)]
        for robot in robots:
            robot[0] = (robot[0] + robot[2]) % width
            robot[1] = (robot[1] + robot[3]) % height
        pass

        for robot in robots:
            grid[robot[1]][robot[0]] += 1
        
        if find_line(grid, 10): # If ten robots are in a line, it's likely the solution...
            print(iteration + 1)
            break
    print_grid(grid)
    pass

result = timeit.timeit('solve_test_input()', setup='from __main__ import solve_test_input', number=1)
print("Example ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
