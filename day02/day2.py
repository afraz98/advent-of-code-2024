import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def test_strictly_increasing(deltas):
    return all([deltas[i] < deltas[i+1] for i in range(0, len(deltas) - 1)])

def test_strictly_decreasing(deltas):
    return all([deltas[i] > deltas[i+1] for i in range(0, len(deltas) - 1)])

def test_report(report):
    return len([x for x in [abs(i) > 3 for i in [report[i] - report[i-1] for i in range(1, len(report))]] if x]) == 0 and (test_strictly_increasing(report) or test_strictly_decreasing(report))

def solve_part_one():
    print(sum([1 if test_report(report) else 0 for report in [[int(r) for r in line.split(" ")] for line in parse_input("day02.txt")]]))

def solve_part_two():
    reports = [[int(r) for r in line.split(" ")] for line in parse_input("day02.txt")]
    safe_reports = 0
    for report in reports:
        if test_report(report):
            safe_reports += 1
        else:
            for i in range(0, len(report)):
                if(test_report(list(filter(lambda x: x != report[i], report)))):
                    safe_reports += 1
    print(safe_reports)

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))

