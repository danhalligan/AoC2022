from aoc2022.helpers import input_str
from aoc2022.tetris import Cave, Shape


def shape_gen():
    shapes = [
        Shape([[1, 1, 1, 1]]),
        Shape([[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
        Shape([[1, 1, 1], [0, 0, 1], [0, 0, 1]]),
        Shape([[1], [1], [1], [1]]),
        Shape([[1, 1], [1, 1]]),
    ]
    seq = list(range(5))
    i = 0
    while True:
        yield shapes[seq[i]]
        i += 1
        if i == len(seq):
            i = 0


def jet_gen(file):
    seq = list(input_str(file))
    i = 0
    while True:
        yield 1 if seq[i] == ">" else -1
        i += 1
        if i == len(seq):
            i = 0


def part1(file):
    jets = jet_gen(file)
    shapes = shape_gen()
    cave = Cave()

    for i in range(2022):
        shape = shapes.__next__()
        shape.pos = [2, cave.top() + 4]
        shape.move(cave, jets)
        cave.alter(shape)

    return cave.top() + 1


def part2(file):
    # By inspection, there's a burn in of 435 blocks, then repeats of length 1710
    jets = jet_gen(file)
    shapes = shape_gen()
    cave = Cave()

    heights = []
    for i in range(2500):
        shape = shapes.__next__()
        shape.pos = [2, cave.top() + 4]
        shape.move(cave, jets)
        cave.alter(shape)
        heights += [cave.top()]

    start = heights[435]
    inc = heights[1710 + 435] - heights[435]
    target = 1000000000000
    nrepeats = (target - 435) // 1710
    remainder = (target - 435) % 1710
    return start + inc * nrepeats + heights[435 + remainder] - start
