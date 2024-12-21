import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def find_combo_operand(operand, registers):
    if operand == 4:
        operand = registers[0]
    elif operand == 5:
        operand = registers[1]
    elif operand == 6:
        operand = registers[2]
    return operand

def run_instructions(instruction_pointer, registers, opcode, operand, output):
    if opcode == 0: # adv
        registers[0] = registers[0] // (2 ** find_combo_operand(operand, registers))
    elif opcode == 1: # bxl
        registers[1] = registers[1] ^ operand
    elif opcode == 2: # bst
        registers[1] = find_combo_operand(operand, registers) % 8
    elif opcode == 3: # jnz
        if registers[0] != 0:
            return operand, output, registers
    elif opcode == 4: # bxc
        registers[1] = registers[1] ^ registers[2]
        pass
    elif opcode == 5: # out
        output.append(find_combo_operand(operand, registers) % 8)
    elif opcode == 6: # bdv
        registers[1] = registers[0] // (2 ** find_combo_operand(operand, registers))
    elif opcode == 7: # cdv
        registers[2] = registers[0] // (2 ** find_combo_operand(operand, registers))
    return instruction_pointer + 2, output, registers


def solve_part_one():
    output = []
    registers = []
    input = parse_input("day17.txt")

    registers.append(int(input[0].replace(" ", "").split(":")[1]))
    registers.append(int(input[1].replace(" ", "").split(":")[1]))
    registers.append(int(input[2].replace(" ", "").split(":")[1]))
    program = [int(opcode) for opcode in input[4].replace(" ", "").split(":")[1].split(",")]

    instruction_pointer = 0
    while instruction_pointer < len(program):
        instruction_pointer, output, registers = run_instructions(instruction_pointer, registers, program[instruction_pointer], program[instruction_pointer+1], output)
    print(','.join([str(x) for x in output]))

def solve_part_two():
    output = []
    registers = []
    input = parse_input("day17.txt")

    registers.append(int(input[0].replace(" ", "").split(":")[1]))
    registers.append(int(input[1].replace(" ", "").split(":")[1]))
    registers.append(int(input[2].replace(" ", "").split(":")[1]))
    program = [int(opcode) for opcode in input[4].replace(" ", "").split(":")[1].split(",")]
    
    i = 100000000
    while(output != program):
        output = []
        registers[0] = i
        print("i = %d" % i)
        instruction_pointer = 0
        while instruction_pointer < len(program):
            instruction_pointer, output, registers = run_instructions(instruction_pointer, registers, program[instruction_pointer], program[instruction_pointer+1], output)
        i = i + 1

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
