from __future__ import annotations
import abc
from typing import List


class Solution:

    def __init__(self, input_lines: List[str]):
        self.input_lines = input_lines

    @abc.abstractmethod
    def solve(self) -> (str, str):
        pass
