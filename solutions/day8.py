from solutions import Solution


class Day8(Solution):

    def solve(self) -> (str, str):
        return self.__calculate_part_1(self.input_lines), self.__calculate_part_2(self.input_lines)

    @staticmethod
    def __calculate_part_1(input_lines):
        input_sum = 0
        actual_sum = 0

        for line in input_lines:
            input_sum += len(line)
            actual_sum += eval(f"len({line})")

        return abs(input_sum - actual_sum)

    @staticmethod
    def __calculate_part_2(input_lines):
        input_sum = 0
        actual_sum = 0

        for line in input_lines:
            input_sum += len(line)
            line = line.replace('\\', r"\\")
            line = line.replace('"', '\\"')
            actual_sum += (len(line) + 2)

        return abs(input_sum - actual_sum)
