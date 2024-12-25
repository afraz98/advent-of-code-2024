import itertools
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

def find_prices(secret_number): # Find sequence of prices (first digit from each secret number)
    prices = []
    for _ in range(2000):
        prices.append(secret_number % 10)
        secret_number = generate_secret_number(secret_number)
    return prices

def calculate_price_deltas(price_list):
    deltas = [0]
    for i in range(1, len(price_list)):
        deltas.append(price_list[i] - price_list[i-1])
    return deltas

def find_sequence(price_deltas, sequence):
    for i in range(3, len(price_deltas)):
        if [price_deltas[i-3], price_deltas[i-2], price_deltas[i-1], price_deltas[i]] == sequence:
            return i
    return -1

def solve_part_two():
    totals = []
    secret_numbers = [int(number) for number in parse_input("day22.txt")]
    price_lists = [find_prices(number) for number in secret_numbers]
    price_deltas = [calculate_price_deltas(price_list) for price_list in price_lists]

    for sequence in [list(x) for x in list(itertools.permutations(range(-9, 10), 4))]:
        print(sequence)
        total = 0
        for j in range(0, len(price_deltas)):
            i = find_sequence(price_deltas[j], sequence)
            if i != -1:
                total += price_lists[j][i]
        totals.append(total)

    print(max(totals))
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
# result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
# print("Part II ran in %s seconds" % str(result))
