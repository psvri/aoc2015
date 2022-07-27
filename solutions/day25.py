import numpy as np

from solutions import Solution


class Day25(Solution):

    def solve(self) -> (str, str):
        input_lines = self.input_lines[0].split(' ')
        row = int(input_lines[16].replace(',', ''))
        column = int(input_lines[18].replace('.', ''))
        max_row = row + column

        sheet = np.full((max_row, max_row), 0)
        base = 20151125
        cur = base

        for i in range(1, max_row + 1):
            sums = self.get_sums(i)
            for comb in sums:
                sheet[comb[0]][comb[1]] = cur
                cur = self.compute(cur, 252533, 33554393)

        return sheet[row - 1][column - 1], 'Machine Started'

    @staticmethod
    def compute(x, mul, divisor):
        return (x * mul) % divisor

    @staticmethod
    def get_sums(x):
        sums = []
        max_sum = x - 1
        base = [max_sum, 0]
        sums.append(base)
        for _ in range(max_sum):
            sums.append([sums[-1][0] - 1, sums[-1][1] + 1])

        return sums
