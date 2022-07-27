import numpy as np
import enum
from collections import defaultdict
from solutions import Solution


class Operations(enum.Enum):
    LSHIFT = '<<'
    RSHIFT = '>>'
    NOT = '~'
    AND = '&'
    OR = '|'


class Day7(Solution):

    def solve(self) -> (str, str):
        current_states = defaultdict(np.ushort)
        self.__simulate_circuit(current_states, self.input_lines)
        part1_answer = current_states['a']

        for i in range(len(self.input_lines)):
            if self.input_lines[i].endswith('-> b'):
                self.input_lines[i] = f"{current_states['a']} -> b"
                break

        current_states = defaultdict(np.ushort)
        self.__simulate_circuit(current_states, self.input_lines)
        return part1_answer, current_states['a']

    @classmethod
    def __simulate_circuit(cls, current_states, circuit_steps):
        while len(circuit_steps) != 0:
            completed_list_indexes = []
            for i in range(len(circuit_steps)):
                step = circuit_steps[i]
                size = len(step.split(' '))
                if size == 3:
                    lhs, rhs = step.split(' -> ')
                    if lhs.isnumeric():
                        current_states[rhs] = np.ushort(lhs)
                        completed_list_indexes.append(i)
                    elif lhs in current_states:
                        current_states[rhs] = current_states[lhs]
                        completed_list_indexes.append(i)
                if size == 4:
                    operation, lhs, _, rhs = step.split(' ')
                    if lhs in current_states:
                        eval_string = f"{Operations.NOT.value}current_states[lhs]"
                        current_states[rhs] = eval(eval_string)
                        completed_list_indexes.append(i)
                if size == 5:
                    lhs1, operation, lhs2, _, rhs = step.split(' ')
                    if operation == Operations.LSHIFT.name or operation == Operations.RSHIFT.name:
                        if lhs1 in current_states:
                            eval_string = f"current_states[lhs1]{Operations[operation].value}np.ushort(lhs2)"
                            current_states[rhs] = eval(eval_string)
                            completed_list_indexes.append(i)
                    else:
                        if lhs1 in current_states and lhs2 in current_states:
                            eval_string = f"current_states[lhs1]{Operations[operation].value}current_states[lhs2]"
                            current_states[rhs] = eval(eval_string)
                            completed_list_indexes.append(i)
                        elif lhs1.isnumeric() and lhs2 in current_states:
                            eval_string = f"np.ushort(lhs1){Operations[operation].value}current_states[lhs2]"
                            current_states[rhs] = eval(eval_string)
                            completed_list_indexes.append(i)
                        elif lhs2.isnumeric() and lhs1 in current_states:
                            eval_string = f"np.ushort(lhs2){Operations[operation].value}current_states[lhs1]"
                            current_states[rhs] = eval(eval_string)
                            completed_list_indexes.append(i)

            new_list = []
            for index, val in enumerate(circuit_steps):
                if index not in completed_list_indexes:
                    new_list.append(val)

            circuit_steps = new_list
