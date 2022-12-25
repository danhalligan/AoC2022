from aoc2022.helpers import input_lines


def desnaf(x):
    m = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    return sum(5**i * m[v] for i, v in enumerate(x[::-1]))


def ensnaf(x):
    m2 = {0: "0", 1: "1", 2: "2", 3: "=", 4: "-", 5: "0"}
    s = ""
    while x != 0:
        r = x % 5
        x = x // 5 + (r in [3, 4])
        s = m2[r] + s
    return s


def part1(file):
    lines = input_lines(file)
    return ensnaf(sum(desnaf(line) for line in lines))


def part2(file):
    return None
