import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def mix(secret, N):
    return secret ^ N

def prune(secret):
    return secret % 16777216

def generate_secret_number(initial):
    initial = prune(mix(initial, initial * 64))
    initial = prune(mix(initial, initial // 32))
    initial = prune(mix(initial, initial * 2048))
    return initial

def solve_part_one():
    secret_numbers = [int(number) for number in parse_input("day22.txt")]
    
    for i in range(0, len(secret_numbers)):
        for _ in range(2000):
            secret_numbers[i] = generate_secret_number(secret_numbers[i])
    print(sum(secret_numbers))
    pass

def solve_part_two():
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
