from copy import copy
from dataclasses import dataclass
from enum import Enum, auto
from math import inf

from solutions import Solution


class ItemType(Enum):
    Weapons = auto()
    Armor = auto()
    Ring = auto()


@dataclass
class Item:
    type: ItemType
    name: str
    cost: int
    damage: int
    armor: int


@dataclass
class HittableEntity:
    hit_points: int
    damage: int
    armor: int

    def gets_hit(self, another_hittable: 'HittableEntity'):
        self.hit_points -= max(1, another_hittable.damage - self.armor)


class Player(HittableEntity):
    pass


class Boss(HittableEntity):
    pass


WEAPONS = [
    Item(ItemType.Weapons, 'Dagger', 8, 4, 0),
    Item(ItemType.Weapons, 'Shortsword', 10, 5, 0),
    Item(ItemType.Weapons, 'Warhammer', 25, 6, 0),
    Item(ItemType.Weapons, 'Longsword', 40, 7, 0),
    Item(ItemType.Weapons, 'Greataxe', 74, 8, 0),
]

ARMORS = [
    Item(ItemType.Armor, 'DUMMYARMOR', 0, 0, 0),
    Item(ItemType.Armor, 'Leather', 13, 0, 1),
    Item(ItemType.Armor, 'Chainmail', 31, 0, 2),
    Item(ItemType.Armor, 'Splintmail', 53, 0, 3),
    Item(ItemType.Armor, 'Bandedmail', 75, 0, 4),
    Item(ItemType.Armor, 'Platemail', 102, 0, 5),
]

RINGS = [
    Item(ItemType.Armor, 'DUMMYRING1', 0, 0, 0),
    Item(ItemType.Armor, 'DUMMYRING2', 0, 0, 0),
    Item(ItemType.Ring, 'Damage +1', 25, 1, 0),
    Item(ItemType.Ring, 'Damage +2', 50, 2, 0),
    Item(ItemType.Ring, 'Damage +3', 100, 3, 0),
    Item(ItemType.Ring, 'Defense +1', 20, 0, 1),
    Item(ItemType.Ring, 'Defense +2', 40, 0, 2),
    Item(ItemType.Ring, 'Defense +3', 80, 0, 3),
]


class Day21(Solution):

    def solve(self) -> (str, str):
        data = self.input_lines

        boss_hit_points = int(data[0].split(': ')[1])
        boss_damage = int(data[1].split(': ')[1])
        boss_armor = int(data[2].split(': ')[1])
        boss = Boss(boss_hit_points, boss_damage, boss_armor)

        return self.__compute_part1(boss), self.__compute_part2(boss)

    @staticmethod
    def __simulate(player: Player, boss: Boss):
        player_turn = True

        while player.hit_points > 0 and boss.hit_points > 0:
            if player_turn:
                boss.gets_hit(player)
                player_turn = False
            else:
                player.gets_hit(boss)
                player_turn = True

    def __compute_part1(self, boss: Boss):
        min_cost = inf
        for weapon in WEAPONS:
            for armor in ARMORS:
                for i in range(0, len(RINGS) - 1):
                    for j in range(i + 1, len(RINGS)):
                        total_player_armor = weapon.armor + armor.armor + RINGS[i].armor + RINGS[j].armor
                        total_player_damage = weapon.damage + armor.damage + RINGS[i].damage + RINGS[j].damage
                        player = Player(100, total_player_damage, total_player_armor)
                        boss_copy = copy(boss)
                        self.__simulate(player, boss_copy)
                        if boss_copy.hit_points <= 0:
                            total_cost = weapon.cost + armor.cost + RINGS[i].cost + RINGS[j].cost
                            min_cost = min(min_cost, total_cost)

        return min_cost

    def __compute_part2(self, boss: Boss):
        max_cost = -inf
        for weapon in WEAPONS:
            for armor in ARMORS:
                for i in range(0, len(RINGS) - 1):
                    for j in range(i + 1, len(RINGS)):
                        total_player_armor = weapon.armor + armor.armor + RINGS[i].armor + RINGS[j].armor
                        total_player_damage = weapon.damage + armor.damage + RINGS[i].damage + RINGS[j].damage
                        player = Player(100, total_player_damage, total_player_armor)
                        boss_copy = copy(boss)
                        self.__simulate(player, boss_copy)
                        if player.hit_points <= 0:
                            total_cost = weapon.cost + armor.cost + RINGS[i].cost + RINGS[j].cost
                            max_cost = max(max_cost, total_cost)

        return max_cost
