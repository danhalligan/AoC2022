import re
from aoc2022.helpers import input_lines
from copy import deepcopy
from heapq import heappush, heappop
from functools import cache


def data(file):
    lines = input_lines(file)
    blizzards = []
    for i, line in enumerate(lines[1:-1]):
        for m in re.finditer("[<>^v]", line):
            blizzards.append({"pos": (i, m.start() - 1), "shape": m.group()})
    dim = (len(lines) - 2, len(lines[0]) - 2)
    start = re.search(r"\.", lines[0]).start() - 1
    end = re.search(r"\.", lines[-1]).start() - 1
    return dim, blizzards, (-1, start), (dim[0], end)


def update(blizzards, dim):
    blizzards = deepcopy(blizzards)
    for x in blizzards:
        if x["shape"] == ">":
            x["pos"] = (x["pos"][0], (x["pos"][1] + 1) % dim[1])
        elif x["shape"] == "<":
            x["pos"] = (x["pos"][0], (x["pos"][1] - 1) % dim[1])
        if x["shape"] == "^":
            x["pos"] = ((x["pos"][0] - 1) % dim[0], x["pos"][1])
        if x["shape"] == "v":
            x["pos"] = ((x["pos"][0] + 1) % dim[0], x["pos"][1])
    return blizzards


@cache
def tblizzards(time):
    if time == 0:
        return blizzards
    else:
        return update(tblizzards(time - 1), dim)


def neighbours(pos, dim):
    p = [
        (pos[0] - 1, pos[1]),
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] - 1),
        (pos[0], pos[1] + 1),
    ]
    p = [x for x in p if 0 <= x[0] < dim[0] and 0 <= x[1] < dim[1]]
    if pos == (end[0] - 1, end[1]):
        p += [end]
    if pos == (start[0] + 1, start[1]):
        p += [start]
    return p


def dist(loc, end):
    return abs(loc[0] - end[0]) + abs(loc[1] - end[1])


def moves(loc, time, dest):
    bp = [x["pos"] for x in tblizzards(time + 1)]
    poss = [loc] + neighbours(loc, dim)
    return [x for x in poss if x not in bp or x in dest]


def solve(begin, dest, time):
    loc = begin
    q = []
    heappush(q, [0, time, loc])
    best = 10000000000
    time = 0
    seen = {}
    while q:
        _, time, loc = heappop(q)
        if time >= best or (time, loc) in seen:
            continue
        seen[time, loc] = True
        if loc == dest:
            best = min(best, time)
        for p in moves(loc, time, dest):
            heappush(q, [dist(loc, dest) + (time + 1), time + 1, p])
    return best


dim, blizzards, start, end = data("inputs/day24.txt")


def part1(file):
    return solve(start, end, 0)


def part2(file):
    t1 = solve(start, end, 0)
    t2 = solve(end, start, t1)
    return solve(start, end, t2)
