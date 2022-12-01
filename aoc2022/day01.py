from aoc2022.helpers import *


def totals(file):
    return [sum(map(int, elf)) for elf in input_blocks(file)]


def part1(file):
    return max(totals(file))


def part2(file):
    return sum(sorted(totals(file))[-3:])
