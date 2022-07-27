from solutions import Solution


class Day2(Solution):
    def solve(self) -> (str, str):
        total_sheet = 0
        total_ribbon = 0
        for line in self.input_lines:
            line = line.strip()
            l, b, h = [int(i) for i in line.split('x')]
            total_sheet += self._sheet(l, b, h)

            total_ribbon += self._ribbon(l, b, h)

        return total_sheet, total_ribbon

    @staticmethod
    def _sheet(l, b, h):
        areas = [l * b, b * h, h * l]
        return min(areas) + 2 * sum(areas)

    @staticmethod
    def _ribbon(l, b, h):
        perimeters = [l + b, b + h, h + l]
        return l * b * h + 2 * min(perimeters)
