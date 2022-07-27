from itertools import permutations
import math

from solutions import Solution


class Day9(Solution):

    def solve(self) -> (str, str):
        cities = set()
        weights = {}

        for line in self.input_lines:
            values = line.split(' ')
            cities.add(values[0])
            cities.add(values[2])
            weights[(values[0], values[2])] = int(values[4])
            weights[(values[2], values[0])] = int(values[4])

        max_distance = -math.inf
        min_distance = math.inf
        routes = list(permutations(cities))

        for route in routes:
            distance = 0
            for i in range(len(route) - 1):
                distance += weights[(route[i], route[i + 1])]

            if distance < min_distance:
                min_distance = distance
            if distance > max_distance:
                max_distance = distance

        return min_distance, max_distance
