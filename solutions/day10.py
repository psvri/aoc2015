from solutions import Solution


class Day10(Solution):
    ITERATION_COUNT = 50

    def solve(self) -> (str, str):
        input_no = self.input_lines[0]
        for _ in range(40):
            input_no = self.__convert_no(input_no)

        part1_answer = len(input_no)

        for _ in range(10):
            input_no = self.__convert_no(input_no)

        return part1_answer, len(input_no)

    @staticmethod
    def __convert_no(x):
        new_no = ''
        str_index = 0
        while str_index < len(x):
            current = x[str_index]
            count = 0
            i = str_index
            while i < len(x) and x[i] == current:
                i += 1
                count += 1
            str_index += count
            new_no += str(count) + current

        return new_no
