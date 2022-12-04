from aoc2022.helpers import input_lines, ints
import re


def contains(x1, x2, y1, y2):
    return (y1 >= x1 and y2 <= x2) or (x1 >= y1 and x2 <= y2)


def overlaps(x1, x2, y1, y2):
    return (y1 >= x1 and y1 <= x2) or (x1 >= y1 and x1 <= y2)


def part1(file):
    dat = [ints(re.findall("\\d+", line)) for line in input_lines(file)]
    return sum(contains(*x) for x in dat)


def part2(file):
    dat = [ints(re.findall("\\d+", line)) for line in input_lines(file)]
    return sum(overlaps(*x) for x in dat)
