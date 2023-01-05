class CPU:
    def __init__(self, program_file):
        with open(program_file, 'r') as f:
            self.program = [line.strip().split() for line in f]
        self.x = 1
        self.pc = 0
        self.cycles = 0
        self.history = [(0, self.x)]  # (cycle, x) tuples

    def run(self):
        while self.pc < len(self.program):
            self.execute_instruction(self.program[self.pc])

    def execute_instruction(self, instruction):
        if instruction[0] == 'addx':
            self.x += int(instruction[1])
            self.pc += 1
            self.cycles += 2
            self.history.append((self.cycles, self.x))
        elif instruction[0] == 'noop':
            self.pc += 1
            self.cycles += 1
            self.history.append((self.cycles, self.x))
        else:
            raise ValueError(f'Invalid instruction: {instruction[0]}')

cpu = CPU('program.txt')
cpu.run()

for cycle, x in cpu.history:
    if cycle == 20 or cycle % 40 == 0:
        print(f'Cycle {cycle}: X = {x}')
