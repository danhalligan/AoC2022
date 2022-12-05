from aoc2022.helpers import ints
import re


def data(file):
    dat = open(file).read().split("\n\n")

    lines = dat[0].split("\n")
    p = list(range(1, len(lines[0]), 4))
    crates = [[line[x] for x in p] for line in lines]
    crates = list(map(list, zip(*crates)))
    crates = [x[:-1] for x in crates]
    crates = [[x for x in line if x != " "] for line in crates]

    instructions = dat[1].rstrip().split("\n")

    return crates, instructions


def part1(file):
    crates, instructions = data(file)
    for line in instructions:
        n, f, t = ints(re.findall(r"\d+", line))
        crates[t - 1] = crates[f - 1][:n][::-1] + crates[t - 1]
        crates[f - 1] = crates[f - 1][n:]
    return "".join(x[0] for x in crates)


def part2(file):
    crates, instructions = data(file)
    for line in instructions:
        n, f, t = ints(re.findall(r"\d+", line))
        crates[t - 1] = crates[f - 1][:n] + crates[t - 1]
        crates[f - 1] = crates[f - 1][n:]
    return "".join(x[0] for x in crates)
