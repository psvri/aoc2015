from collections import defaultdict
from itertools import permutations
import math

import enum

from solutions import Solution


class Change(enum.Enum):
    gain = +1
    lose = -1


class Day13(Solution):

    def solve(self) -> (str, str):
        characters = set()
        happiness_score = defaultdict(int)

        for line in self.input_lines:
            line = line[:-1]

            character1, _, stats, score, _, _, _, _, _, _, charecter2 = line.split(' ')
            characters.add(character1)
            characters.add(charecter2)

            happiness_score[(character1, charecter2)] = Change[stats].value * int(score)

        possible_solutions = permutations(characters)
        part1_answer = self.__get_max_value(possible_solutions, happiness_score)

        me = 'me'
        for character in characters:
            happiness_score[(character, me)] = 0
            happiness_score[(me, character)] = 0
        characters.add(me)

        possible_solutions = permutations(characters)

        return part1_answer, self.__get_max_value(possible_solutions, happiness_score)

    @staticmethod
    def __get_max_value(possible_solutions, happiness_score):
        max_val = -math.inf

        for solution in possible_solutions:
            score = 0

            for i in range(len(solution) - 1):
                score += happiness_score[(solution[i], solution[i + 1])] + happiness_score[
                    (solution[i + 1], solution[i])]

            score += happiness_score[(solution[0], solution[-1])] + happiness_score[(solution[-1], solution[0])]

            if score > max_val:
                max_val = score

        return max_val
