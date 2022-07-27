from solutions import Solution


class Day1(Solution):

    def solve(self) -> (str, str):
        pos: int = 0
        first_negative_found = False
        part2_answer = 0
        for index, step in enumerate(self.input_lines[0]):
            if step == ')':
                pos = pos - 1
            else:
                pos = pos + 1
            if pos < 0 and not first_negative_found:
                part2_answer = index + 1
                first_negative_found = True

        return pos, part2_answer
