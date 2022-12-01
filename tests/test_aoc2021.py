import importlib
import pytest
from aoc2022.helpers import *

solutions = [(1, [24000, 45000])]

# Test each day by importing the module and running part1 and part2
@pytest.mark.parametrize("day,expected", solutions)
def test_all(day, expected):
    module = importlib.import_module(f"aoc2022.day{day:02d}")
    file = "tests/inputs/day" + f"{day:02d}" + ".txt"
    assert getattr(module, "part1")(file) == expected[0]
    assert getattr(module, "part2")(file) == expected[1]
