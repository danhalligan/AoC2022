import importlib
import pytest

solutions = [
    (1, [24000, 45000]),
    (2, [15, 12]),
    (3, [157, 70]),
    (4, [2, 4]),
    (5, ["CMZ", "MCD"]),
    (6, [11, 26]),
    (7, [95437, 24933642]),
    (8, [21, 8]),
    (9, [13, 1]),
    (10, [13140, None]),
    (11, [10605, 2713310158]),
    (12, [31, 29]),
    (13, [13, 140]),
]


# Test each day by importing the module and running part1 and part2
@pytest.mark.parametrize("day,expected", solutions)
def test_all(day, expected):
    module = importlib.import_module(f"aoc2022.day{day:02d}")
    file = "tests/inputs/day" + f"{day:02d}" + ".txt"
    assert getattr(module, "part1")(file) == expected[0]
    assert getattr(module, "part2")(file) == expected[1]
