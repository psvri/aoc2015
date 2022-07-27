import numpy as np
from solutions import Solution


class Day6(Solution):

    def solve(self) -> (str, str):
        lights = np.full((1000, 1000), False)

        for step in self.input_lines:
            if 'turn on' in step:
                step = step.replace('turn on ', '')
                x1, y1 = [int(i) for i in step.split(' ')[0].split(',')]
                x2, y2 = [int(i) for i in step.split(' ')[2].split(',')]
                lights[x1:x2 + 1, y1:y2 + 1] = True
            elif 'turn off' in step:
                step = step.replace('turn off ', '')
                x1, y1 = [int(i) for i in step.split(' ')[0].split(',')]
                x2, y2 = [int(i) for i in step.split(' ')[2].split(',')]
                lights[x1:x2 + 1, y1:y2 + 1] = False
            elif 'toggle' in step:
                step = step.replace('toggle ', '')
                x1, y1 = [int(i) for i in step.split(' ')[0].split(',')]
                x2, y2 = [int(i) for i in step.split(' ')[2].split(',')]
                lights[x1:x2 + 1, y1:y2 + 1] = np.logical_not(lights[x1:x2 + 1, y1:y2 + 1])

        part1_answer = np.sum(lights)

        lights = np.full((1000, 1000), 0)
        for step in self.input_lines:
            if 'turn on' in step:
                step = step.replace('turn on ', '')
                x1, y1 = [int(i) for i in step.split(' ')[0].split(',')]
                x2, y2 = [int(i) for i in step.split(' ')[2].split(',')]
                lights[x1:x2 + 1, y1:y2 + 1] += 1
            elif 'turn off' in step:
                step = step.replace('turn off ', '')
                x1, y1 = [int(i) for i in step.split(' ')[0].split(',')]
                x2, y2 = [int(i) for i in step.split(' ')[2].split(',')]
                lights[x1:x2 + 1, y1:y2 + 1] = np.clip(lights[x1:x2 + 1, y1:y2 + 1] - 1, 0, None)
            elif 'toggle' in step:
                step = step.replace('toggle ', '')
                x1, y1 = [int(i) for i in step.split(' ')[0].split(',')]
                x2, y2 = [int(i) for i in step.split(' ')[2].split(',')]
                lights[x1:x2 + 1, y1:y2 + 1] += 2

        return part1_answer, np.sum(lights)
