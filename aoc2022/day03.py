from aoc2022.helpers import input_lines
from functools import reduce


def priority(x):
    base = 38 if x.isupper() else 96
    return ord(x) - base


def part1(file):
    sum = 0
    for line in input_lines(file):
        h = len(line) // 2
        a, b = line[:h], line[h:]
        sum += priority(list(set(a) & set(b))[0])
    return sum


def part2(file):
    lines = input_lines(file)
    sum = 0
    for i in range(0, len(lines), 3):
        x = lines[i : i + 3]
        ch = list(reduce(set.intersection, map(set, x)))[0]
        sum += priority(ch)
    return sum
