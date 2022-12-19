from aoc2022.helpers import input_lines, ints
from collections import defaultdict
import sys


def neighbours(i, j, k):
    return [
        (i - 1, j, k),
        (i, j - 1, k),
        (i, j, k - 1),
        (i + 1, j, k),
        (i, j + 1, k),
        (i, j, k + 1),
    ]


def data(file):
    blocks = defaultdict(bool)
    for line in input_lines(file):
        blocks[tuple(ints(line.split(",")))] = True
    return blocks


def part1(file):
    blocks = data(file)
    tot = 0
    for block in list(blocks.keys()):
        tot += 6 - sum(blocks[x] for x in neighbours(*block))
    return tot


def part2(file):
    sys.setrecursionlimit(10000)

    blocks = data(file)
    blockpos = list(blocks.keys())
    minp = blockpos[0]
    maxp = blockpos[0]
    for p in blockpos:
        minp = [min(x, y - 1) for x, y in zip(minp, p)]
        maxp = [max(x, y + 1) for x, y in zip(maxp, p)]

    def fill(x):
        water[x] = True
        nbs = neighbours(*x)
        nbs = [x for x in nbs if all(p1 >= p2 for p1, p2 in zip(x, minp))]
        nbs = [x for x in nbs if all(p1 <= p2 for p1, p2 in zip(x, maxp))]
        nbs = [x for x in nbs if x not in blockpos]
        nbs = [x for x in nbs if x not in water.keys()]
        for nb in nbs:
            fill(nb)

    water = defaultdict(bool)
    start = tuple(minp)
    fill(start)

    tot = 0
    for block in list(blocks.keys()):
        tot += sum(water[x] for x in neighbours(*block))

    return tot
