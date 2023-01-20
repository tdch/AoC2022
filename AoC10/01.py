class CPU:
    def __init__(self, program_file):
        with open(program_file, 'r') as f:
            self.program = [line.strip().split() for line in f]
        self.x = 1      # X registry
        self.pc = 0     # the position of the current instruction in the program list.
        self.cycles = 0 # the number of cycles that have been executed so far.
        self.history = [(0, self.x, 0)]  # (cycle, x, signal) tuples

    def run(self):
        while self.pc < len(self.program):
            self.execute_instruction(self.program[self.pc])

    def execute_instruction(self, instruction):
        if instruction[0] == 'addx':
            #first part of instruction
            self.cycles += 1
            self.history.append((self.cycles, self.x, (self.cycles+1) * self.x))
            #second part of instruction
            self.x += int(instruction[1])
            self.pc += 1
            self.cycles += 1
            self.history.append((self.cycles, self.x, (self.cycles+1) * self.x))
        elif instruction[0] == 'noop':
            self.pc += 1
            self.cycles += 1
            self.history.append((self.cycles, self.x, (self.cycles+1) * self.x))
        else:
            raise ValueError(f'Invalid instruction: {instruction[0]}')

# Run the program
cpu = CPU('input.txt')
cpu.run()

# Display the signal strength at each of the specified cycles
cycle = 0
razem=0
for _, x, signal in cpu.history:
    cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220, 260]:
        razem += signal
        print(f'Cycle {cycle}: X = {x}, Signal = {signal}')
print(f'Total: Signal = {razem}')
