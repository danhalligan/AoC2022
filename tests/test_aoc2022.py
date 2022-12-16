import importlib
import pytest

solutions = [
    (1, [24000, 45000], [{}, {}]),
    (2, [15, 12], [{}, {}]),
    (3, [157, 70], [{}, {}]),
    (4, [2, 4], [{}, {}]),
    (5, ["CMZ", "MCD"], [{}, {}]),
    (6, [11, 26], [{}, {}]),
    (7, [95437, 24933642], [{}, {}]),
    (8, [21, 8], [{}, {}]),
    (9, [13, 1], [{}, {}]),
    (10, [13140, None], [{}, {}]),
    (11, [10605, 2713310158], [{}, {}]),
    (12, [31, 29], [{}, {}]),
    (13, [13, 140], [{}, {}]),
    (14, [24, 93], [{}, {}]),
    (15, [26, 56000011], [{"row": 10}, {"n": 20}]),
    (16, [1651, 1707], [{}, {}]),
]


# Test each day by importing the module and running part1 and part2
@pytest.mark.parametrize("day,expected,extra", solutions)
def test_all(day, expected, extra):
    module = importlib.import_module(f"aoc2022.day{day:02d}")
    file = "tests/inputs/day" + f"{day:02d}" + ".txt"
    assert getattr(module, "part1")(file, **extra[0]) == expected[0]
    assert getattr(module, "part2")(file, **extra[1]) == expected[1]
