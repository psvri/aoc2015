from enum import Enum

from solutions import Solution


class Instructions(Enum):
    HLF = 'hlf'
    TPL = 'tpl'
    INC = 'inc'
    JMP = 'jmp'
    JIE = 'jie'
    JIO = 'jio'


class Registers(Enum):
    A = 'a'
    B = 'b'


class Computer:
    def __init__(self, instructions, instruction_position=0, initial_value=(0, 0)) -> None:
        self.register_values = {}
        self.instruction_position = instruction_position
        for register in Registers:
            self.register_values[register] = 0
        self.register_values[Registers('a')], self.register_values[Registers('b')] = initial_value
        self.instructions = instructions

    def __increment_instruction_position(self, offset=1):
        self.instruction_position += offset

    def __hlf_operation(self, register):
        self.register_values[Registers(register)] /= 2
        self.__increment_instruction_position()

    def __inc_operation(self, register):
        self.register_values[Registers(register)] += 1
        self.__increment_instruction_position()

    def __tpl_operation(self, register):
        self.register_values[Registers(register)] *= 3
        self.__increment_instruction_position()

    def __jmp_operation(self, offset: int):
        self.__increment_instruction_position(offset)

    def __jie_operation(self, register, offset: int):
        if self.register_values[Registers(register)] % 2 == 0:
            self.__increment_instruction_position(offset)
        else:
            self.__increment_instruction_position()

    def __jio_operation(self, register, offset: int):
        if self.register_values[Registers(register)] == 1:
            self.__increment_instruction_position(offset)
        else:
            self.__increment_instruction_position()

    def compute(self):
        while self.instruction_position < len(self.instructions):
            instruction_details = self.instructions[self.instruction_position].split(' ')
            instruction = Instructions(instruction_details[0])
            if instruction == Instructions.HLF:
                self.__hlf_operation(instruction_details[1])
            elif instruction == Instructions.TPL:
                self.__tpl_operation(instruction_details[1])
            elif instruction == Instructions.INC:
                self.__inc_operation(instruction_details[1])
            elif instruction == Instructions.JMP:
                self.__jmp_operation(int(instruction_details[1]))
            elif instruction == Instructions.JIE:
                self.__jie_operation(instruction_details[1].replace(',', ''), int(instruction_details[2]))
            elif instruction == Instructions.JIO:
                self.__jio_operation(instruction_details[1].replace(',', ''), int(instruction_details[2]))


class Day23(Solution):

    def solve(self) -> (str, str):
        input_instructions = self.input_lines
        computer = Computer(input_instructions)
        computer.compute()
        part1_answer = computer.register_values[Registers.B]
        computer = Computer(input_instructions, initial_value=(1, 0))
        computer.compute()
        return part1_answer, computer.register_values[Registers.B]
