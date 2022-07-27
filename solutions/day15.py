from copy import deepcopy, copy
from functools import reduce
from typing import Set, Dict, Callable

from dataclasses import dataclass, field
from enum import Enum
from collections import defaultdict
from math import inf

from solutions import Solution


class Properties(Enum):
    capacity = 'capacity'
    durability = 'durability'
    flavor = 'flavor'
    texture = 'texture'
    calories = 'calories'


@dataclass(unsafe_hash=True)
class Ingredient:
    name: str = field(init=False)
    properties: defaultdict = field(default_factory=lambda: defaultdict(int), compare=False, hash=False)


class Day15(Solution):

    def solve(self) -> (str, str):
        ingredients = self.__create_ingredients(self.input_lines)

        return self.__compute(deepcopy(ingredients), 100, defaultdict(int), self.__compute_score_part1), \
               self.__compute(ingredients, 100, defaultdict(int), self.__compute_score_part2)

    @staticmethod
    def __compute_score_part1(ingredients_usage: Dict[Ingredient, int]) -> int:
        required_properties = [Properties.capacity, Properties.durability, Properties.flavor, Properties.texture]
        accumulated_property_score = defaultdict(int)
        for ingredient, weight in ingredients_usage.items():
            for required_property in required_properties:
                accumulated_property_score[required_property] += (ingredient.properties[required_property] * weight)

        values = [max(0, a) for a in accumulated_property_score.values()]
        return reduce(lambda a, b: a * b, values)

    def __compute_score_part2(self, ingredients_usage: Dict[Ingredient, int]) -> int:
        total_calories = 0
        for ingredient, weight in ingredients_usage.items():
            total_calories += (ingredient.properties[Properties.calories]) * weight

        if total_calories == 500:
            return self.__compute_score_part1(ingredients_usage)
        else:
            return 0

    @staticmethod
    def __create_ingredients(lines) -> Set[Ingredient]:
        input_ingredients = set()
        for line in lines:
            ingredient = Ingredient()
            ingredient.name, ingredient_factors = line.split(': ')
            for factor in ingredient_factors.split(', '):
                factor_name, factor_value = factor.split(' ')
                ingredient.properties[Properties(factor_name)] = int(factor_value)
                input_ingredients.add(ingredient)

        return input_ingredients

    def __compute(self, avail_ingredients: Set[Ingredient], avail_weight: int,
                  used_ingredients: Dict[Ingredient, int],
                  score_function: Callable[[Dict[Ingredient, int]], int]) -> int:
        if avail_weight == 0:
            return self.__compute_score_part1(used_ingredients)
        elif len(avail_ingredients) == 1:
            used_ingredients[avail_ingredients.pop()] = avail_weight
            return score_function(used_ingredients)
        else:
            ingredient = avail_ingredients.pop()
            new_used_ingredients = deepcopy(used_ingredients)
            new_used_ingredients[ingredient] = 0
            result = -inf
            for i in range(0, avail_weight + 1):
                result = max(result, self.__compute(copy(avail_ingredients), avail_weight - i, new_used_ingredients,
                                                    score_function))
                new_used_ingredients[ingredient] += 1
            return result
