from aoc2022.helpers import ints
from collections import defaultdict


def build_cave(dat):
    cave = defaultdict(lambda: 0)
    for line in dat:
        coords = line.split(" -> ")
        for f, t in zip(coords, coords[1:]):
            a1, b1 = ints(f.split(","))
            a2, b2 = ints(t.split(","))
            if a1 == a2:
                b1, b2 = sorted([b1, b2])
                for y in range(b1, b2 + 1):
                    cave[a1, y] = 1
            if b1 == b2:
                a1, a2 = sorted([a1, a2])
                for x in range(a1, a2 + 1):
                    cave[x, b1] = 1
    return cave


def print_cave(cave, xmin=492, xmax=507, height=10):
    for y in range(height):
        row = [{0: ".", 1: "#", 2: "o"}[cave[x, y]] for x in range(xmin, xmax)]
        print("".join(row))


def maxcave(cave):
    return max(y for x, y in cave.keys() if cave[x, y] == 1)


def drop_and_roll(cave, grain):
    while cave[grain[0], grain[1] + 1] == 0:
        grain[1] += 1
        if grain[1] > maxcave(cave):
            raise Exception()
    if cave[grain[0] - 1, grain[1] + 1] == 0:
        grain = [grain[0] - 1, grain[1] + 1]
        return drop_and_roll(cave, grain)
    elif cave[grain[0] + 1, grain[1] + 1] == 0:
        grain = [grain[0] + 1, grain[1] + 1]
        return drop_and_roll(cave, grain)
    else:
        return tuple(grain)


def part1(file):
    dat = open(file).read().splitlines()
    cave = build_cave(dat)
    count = 0
    while True:
        try:
            cave[drop_and_roll(cave, [500, 0])] = 2
        except Exception:
            break
        count += 1
    return count


def drop_and_roll2(cave, grain, lim):
    while cave[grain[0], grain[1] + 1] == 0 and grain[1] + 1 <= lim:
        grain[1] += 1
    if grain[1] == lim:
        return tuple(grain)
    if cave[grain[0] - 1, grain[1] + 1] == 0:
        grain = [grain[0] - 1, grain[1] + 1]
        return drop_and_roll2(cave, grain, lim)
    elif cave[grain[0] + 1, grain[1] + 1] == 0:
        grain = [grain[0] + 1, grain[1] + 1]
        return drop_and_roll2(cave, grain, lim)
    else:
        return tuple(grain)


def part2(file):
    dat = open(file).read().splitlines()
    cave = build_cave(dat)
    count = 0
    while True:
        pos = drop_and_roll2(cave, [500, 0], maxcave(cave) + 1)
        count += 1
        if pos == (500, 0):
            break
        cave[pos] = 2
    return count
