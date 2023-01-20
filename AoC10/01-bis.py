class CPU:
    def __init__(self):
        self.x = 1  # initialize X to 1
        self.cycle = 0  # initialize the cycle counter to 0

    def run(self, program):
        """Execute the instructions in the given program"""
        signal_strengths = []  # initialize an empty list to store the signal strengths
        while self.cycle < len(program):  # continue execution until the end of the program
            instruction = program[self.cycle]  # get the instruction for the current cycle
            if instruction == "noop":
                self.cycle += 1  # increment the cycle counter by 1
            elif instruction.startswith("addx"):
                v = int(instruction.split(" ")[1])  # extract the value of V from the instruction
                self.x += v  # update the value of X
                self.cycle += 2  # increment the cycle counter by 2
            if self.cycle in [20, 60, 100, 140, 180, 220]:  # check if the current cycle is one of the target cycles
                signal_strengths.append(self.cycle * self.x)  # append the signal strength to the list
        return signal_strengths  # return the list of signal strengths

def parse_input(filename):
    # read the instructions from the given file and return them as a list
    with open(filename, "r") as f:
        return [line.strip() for line in f]

def main():
    # read the instructions from the file "input.txt"
    program = parse_input("program-1.txt")

    # create a CPU and run the program on it
    cpu = CPU()
    signal_strengths = cpu.run(program)

    # print the signal strength for the 20th cycle and then every 40th cycle
    for i, strength in enumerate(signal_strengths, start=20):
        print(f"Signal strength at cycle {i}: {strength}")

if __name__ == "__main__":
    main()
