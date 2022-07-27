from copy import deepcopy
from collections import namedtuple

from solutions import Solution

Container = namedtuple('Container', 'id size')
function_calls = 0


class Day17(Solution):

    def solve(self) -> (str, str):
        total = 150

        containers = set([Container(id, int(size.strip())) for id, size in enumerate(self.input_lines)])
        result = set()
        self.__get_possible_ways(containers, total, set(), result)
        part1_answer = len(result)

        lengths = [len(i) for i in result]

        minimum = min(lengths)
        count = len([i for i in lengths if i == minimum])
        return part1_answer, count

    def __get_possible_ways(self, containers: set, required_size, filled_containers: set, result_set: set):
        global function_calls
        function_calls += 1
        current_sum = sum([filled_container.size for filled_container in filled_containers])
        if current_sum == required_size:
            result_set.add(frozenset(filled_containers))
        elif len(containers) != 0:
            new_containers = deepcopy(containers)
            new_filled_containers = deepcopy(filled_containers)
            container = new_containers.pop()
            self.__get_possible_ways(new_containers, required_size, new_filled_containers, result_set)
            new_filled_containers.add(container)
            self.__get_possible_ways(new_containers, required_size, new_filled_containers, result_set)
