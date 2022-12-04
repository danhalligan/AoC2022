from aoc2022.helpers import input_lines, ints
import re


def data(file):
    return [ints(re.findall("\\d+", line)) for line in input_lines(file)]


def contains(x1, x2, y1, y2):
    return (y1 >= x1 and y2 <= x2) or (x1 >= y1 and x2 <= y2)


def overlaps(x1, x2, y1, y2):
    return (y1 >= x1 and y1 <= x2) or (x1 >= y1 and x1 <= y2)


def part1(file):
    return sum(contains(*x) for x in data(file))


def part2(file):
    return sum(overlaps(*x) for x in data(file))
