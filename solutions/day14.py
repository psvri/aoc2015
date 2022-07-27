from solutions import Solution
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass(unsafe_hash=True)
class Deer:
    name: str
    fly_speed: int = field(compare=False)
    fly_duration: int = field(compare=False)
    rest_duration: int = field(compare=False)
    is_resting: bool = field(init=False, compare=False, default=False)
    current_position: int = field(init=False, compare=False, default=0)
    resting_time_left: int = field(init=False, compare=False, default=0)
    flight_duration_left: int = field(init=False, compare=False)

    def __post_init__(self):
        self.flight_duration_left = self.fly_duration

    def update_by_one_sec(self):
        if self.is_resting:
            if self.resting_time_left > 0:
                self.resting_time_left -= 1
            else:
                self.is_resting = False
                self.flight_duration_left = self.fly_duration - 1
                self.current_position += self.fly_speed
        else:
            if self.flight_duration_left > 0:
                self.current_position += self.fly_speed
                self.flight_duration_left -= 1
            else:
                self.is_resting = True
                self.resting_time_left = self.rest_duration - 1


class Day14(Solution):

    def solve(self) -> (str, str):
        seconds = 2503
        deers: list[Deer] = list()
        for line in self.input_lines:
            name, _, _, fly_speed, _, _, fly_duration, _, _, _, _, _, _, rest_duration, _ = line.split(' ')
            deers.append(Deer(name, int(fly_speed), int(fly_duration), int(rest_duration)))

        return (max(list(map(self.__calculate_distance_travelled, deers, [seconds] * len(deers))))), \
               self.__calculate_points(deers, seconds)

    @staticmethod
    def __calculate_points(reindeers: list[Deer], seconds: int):
        points = defaultdict(int)

        for _ in range(seconds):
            for reindeer in reindeers:
                reindeer.update_by_one_sec()

            points[max(reindeers, key=lambda reindeer: reindeer.current_position)] += 1

        return max(points.values())

    @staticmethod
    def __calculate_distance_travelled(reindeer: Deer, seconds: int):
        distance = 0
        timer = 0
        is_resting = False

        while timer < seconds:
            if is_resting:
                timer += reindeer.rest_duration
                is_resting = False
            else:
                duration = min(reindeer.fly_duration, seconds - timer)
                distance += reindeer.fly_speed * duration
                timer += duration
                is_resting = True

        return distance
