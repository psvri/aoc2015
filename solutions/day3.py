from collections import defaultdict
from collections import namedtuple
from typing import Dict

from solutions import Solution


class Day3(Solution):
    point = namedtuple('point', ['x', 'y'])

    def solve(self) -> (str, str):
        input_lines = self.input_lines[0]
        santa_map = defaultdict(int)
        santa_pos = self.point(0, 0)
        santa_map[santa_pos] += 1

        for santa_step in input_lines:
            santa_pos = self.increment_map(santa_map, santa_step, santa_pos)
        part1_answer = len(santa_map.keys())

        # reinitialize for part2
        santa_map = defaultdict(int)
        santa_pos = self.point(0, 0)
        santa_map[santa_pos] += 1

        robo_map = defaultdict(int)
        robo_pos = self.point(0, 0)
        robo_map[robo_pos] += 1

        for i in range(0, len(input_lines), 2):
            santa_step = input_lines[i]
            robo_step = input_lines[i + 1]
            santa_pos = self.increment_map(santa_map, santa_step, santa_pos)
            robo_pos = self.increment_map(robo_map, robo_step, robo_pos)

        return part1_answer, len(set(santa_map.keys()).union(robo_map.keys()))

    def increment_map(self, house_map: Dict, step: str, pos: point):
        if step == '>':
            pos = self.point(pos.x, pos.y + 1)
            house_map[pos] += 1
        elif step == '<':
            pos = self.point(pos.x, pos.y - 1)
            house_map[pos] += 1
        elif step == '^':
            pos = self.point(pos.x + 1, pos.y)
            house_map[pos] += 1
        else:  # down case
            pos = self.point(pos.x - 1, pos.y)
            house_map[pos] += 1

        return pos
