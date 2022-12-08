from aoc2022.helpers import input_lines
import numpy as np


def data(file):
    lines = input_lines(file)
    return np.array([[int(x) for x in line] for line in lines])


def sightlines(dat, i, j):
    return [dat[i, j + 1 :], dat[:i, j][::-1], dat[i + 1 :, j], dat[i, :j][::-1]]


def visible(v, trees):
    if v > max(trees):
        return len(trees)
    else:
        return np.argmax(v <= trees) + 1


def part1(file):
    dat = data(file)
    r, c = dat.shape
    tot = 0
    for i in range(1, r - 1):
        for j in range(1, c - 1):
            tot += dat[i, j] > min([max(x) for x in sightlines(dat, i, j)])
    return tot + 2 * r + 2 * (c - 2)


def part2(file):
    dat = data(file)
    r, c = dat.shape
    best = 0
    for i in range(1, r - 1):
        for j in range(1, c - 1):
            ss = np.prod([visible(dat[i, j], t) for t in sightlines(dat, i, j)])
            best = max(best, ss)
    return best
