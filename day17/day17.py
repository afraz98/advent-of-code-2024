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

def run_program(registers, program, i):
    output = []
    registers[0] = i
    instruction_pointer = 0
    while instruction_pointer < len(program):
        instruction_pointer, output, registers = run_instructions(instruction_pointer, registers, program[instruction_pointer], program[instruction_pointer+1], output)
    return output

def solve_part_one():
    output = []
    registers = []
    input = parse_input("day17.txt")

    registers.append(int(input[0].replace(" ", "").split(":")[1]))
    registers.append(int(input[1].replace(" ", "").split(":")[1]))
    registers.append(int(input[2].replace(" ", "").split(":")[1]))
    program = [int(opcode) for opcode in input[4].replace(" ", "").split(":")[1].split(",")]
    print(','.join([str(x) for x in run_program(registers, program, registers[0])]))

def solve_part_two():
    """
        From u/wurlin_murlin:

        "Making a quine on this machine isn't as complicated as it looks:
        - op out only every reads 0-3 or the last 3 bits of reg A, B, or C
        - reg B and C are only ever set by:
            - xoring with literal 0-7 (ie on low 3 bits)
            - anding with last 3 bits of 0-3 or a reg (ie set to 0-7)
            - rshift of reg A
        - that means the whole program is basically just shifting off reg A,
        mutating the last 3 bits, and outputting it 3 bits at a time.
        - the xor and jump means we can't easily reverse it but above means that
        if you can get 3 bits in A that gives a valid out value, it will
        always output the same 3 bit value if lshifted by 3
    """
    registers = []
    input = parse_input("day17.txt")

    registers.append(int(input[0].replace(" ", "").split(":")[1]))
    registers.append(int(input[1].replace(" ", "").split(":")[1]))
    registers.append(int(input[2].replace(" ", "").split(":")[1]))
    program = [int(opcode) for opcode in input[4].replace(" ", "").split(":")[1].split(",")]
    
    register_a_guess = 0
    for j in reversed(range(len(program))):
        register_a_guess = register_a_guess << 3 # Left shift register A
        while run_program(registers, program, register_a_guess) != program[j:]:
            register_a_guess += 1
    print(register_a_guess)

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))
result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
