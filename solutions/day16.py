from dataclasses import dataclass, field
from collections import defaultdict
from typing import List

from solutions import Solution

ANALYSIS_RESULTS = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


@dataclass(unsafe_hash=True)
class Sue:
    name: str = field(hash=True)
    factors: defaultdict = field(default_factory=lambda: defaultdict(int), compare=False, hash=False)


class Day16(Solution):

    def solve(self) -> (str, str):
        sues = self.__create_sues(self.input_lines)
        return self.__compute_part1(sues), self.__compute_part2(sues)

    @staticmethod
    def __create_sues(lines) -> List[Sue]:
        sues: List[Sue] = []
        for line in lines:
            name_index = line.find(': ')
            sue = Sue(line[:name_index])
            factors = line[name_index + 2:]
            for factor in factors.split(', '):
                factor_name, factor_value = factor.split(': ')
                sue.factors[factor_name] = int(factor_value)

            sues.append(sue)
        return sues

    @staticmethod
    def __compute_part1(sues: List[Sue]):
        matching_set = []

        for factor_name, factor_value in ANALYSIS_RESULTS.items():
            matches = set()
            for sue in sues:
                if factor_name in sue.factors:
                    if sue.factors[factor_name] == factor_value:
                        matches.add(sue)

            matching_set.append(matches)

        score = defaultdict(int)

        for i in matching_set:
            for j in i:
                score[j] += 1

        return max(score, key=lambda k: score[k]).name

    @staticmethod
    def __compute_part2(sues: List[Sue]):
        matching_set = []

        gt_factors = {'cats', 'trees'}
        lt_factors = {'pomeranians', 'goldfish'}
        factors = set(ANALYSIS_RESULTS.keys())
        eq_factors = factors - (lt_factors.union(gt_factors))

        for factor_name in eq_factors:
            matches = set()
            for sue in sues:
                if factor_name in sue.factors:
                    if sue.factors[factor_name] == ANALYSIS_RESULTS[factor_name]:
                        matches.add(sue)

            matching_set.append(matches)

        for factor_name in gt_factors:
            matches = set()
            for sue in sues:
                if factor_name in sue.factors:
                    if sue.factors[factor_name] > ANALYSIS_RESULTS[factor_name]:
                        matches.add(sue)

            matching_set.append(matches)

        for factor_name in lt_factors:
            matches = set()
            for sue in sues:
                if factor_name in sue.factors:
                    if sue.factors[factor_name] < ANALYSIS_RESULTS[factor_name]:
                        matches.add(sue)

            matching_set.append(matches)

        score = defaultdict(int)

        for i in matching_set:
            for j in i:
                score[j] += 1

        return max(score, key=lambda k: score[k]).name
