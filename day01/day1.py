import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def solve_part_one():
    list_a = []
    list_b = []
    input = parse_input('day01.txt')
    for line in input:
        sp = line.split('   ')
        list_a.append(sp[0])
        list_b.append(sp[1])

    list_a = sorted(list_a)
    list_b = sorted(list_b)

    sum = 0
    for i in range(0, len(list_a)):
        sum += abs(int(list_a[i]) - int(list_b[i]))
    print(sum)

def find_count(elem, list):
    count = 0
    for l in list:
        if l == elem:
            count += 1
    return count

def solve_part_two():
    list_a = []
    list_b = []

    input = parse_input('day01.txt')
    for line in input:
        sp = line.split('   ')
        list_a.append(sp[0])
        list_b.append(sp[1])

    score = 0
    for element in list_a:
        score += int(element) * find_count(element, list_b)
    print(score)

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Ran in %s seconds" % str(result))