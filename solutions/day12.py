import json

from solutions import Solution


class Day12(Solution):

    def solve(self) -> (str, str):
        json_data = json.loads(self.input_lines[0])
        return self.__get_sum(json_data), self.__get_sum(json_data, True)

    @staticmethod
    def __is_invalid(json_data: dict):
        return "red" in json_data.values()

    def __get_sum(self, json_data, skip_red: bool = False):
        if isinstance(json_data, list):
            total = 0
            for i in json_data:
                total += self.__get_sum(i, skip_red)
            return total
        elif isinstance(json_data, dict):
            total = 0
            if skip_red:
                if not self.__is_invalid(json_data):
                    for key, val in json_data.items():
                        total = total + self.__get_sum(key, skip_red) + self.__get_sum(val, skip_red)
                return total
            else:
                for key, val in json_data.items():
                    total = total + self.__get_sum(key, skip_red) + self.__get_sum(val, skip_red)
                return total
        elif isinstance(json_data, int):
            return int(json_data)
        elif isinstance(json_data, str):
            return 0
