from aoc2022.helpers import input_lines
from math import inf
from heapq import heappush, heappop
from collections import defaultdict
import string


def find_target(grid, x):
    return list(grid.keys())[list(grid.values()).index(x)]


def parse(file):
    grid = {}
    lines = input_lines(file)
    for r in range(len(lines)):
        row = list(lines[r])
        for c in range(len(row)):
            grid[c, r] = row[c]
    start = find_target(grid, "S")
    end = find_target(grid, "E")
    grid[start] = "a"
    grid[end] = "z"
    letters = dict(zip(list(string.ascii_lowercase), range(26)))
    for pos in grid.keys():
        grid[pos] = letters[grid[pos]]
    return start, end, grid


def neighbours(pos, grid):
    i, j = pos
    nb = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    nb = [x for x in nb if x in grid.keys()]
    return [x for x in nb if grid[x] <= grid[pos] + 1]


def dij(start, grid, nb):
    dist = defaultdict(lambda: inf)
    queue = [(0, start)]
    while queue:
        steps, u = heappop(queue)
        for v in nb(u, grid):
            if dist[v] > steps + 1:
                dist[v] = steps + 1
                heappush(queue, [steps + 1, v])
    return dist


def part1(file):
    start, end, grid = parse(file)
    return dij(start, grid, neighbours)[end]


def neighbours2(pos, grid):
    i, j = pos
    nb = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    nb = [x for x in nb if x in grid.keys()]
    return [x for x in nb if grid[pos] <= grid[x] + 1]


def part2(file):
    start, end, grid = parse(file)
    dist = dij(end, grid, neighbours2)
    return min(dist[pos] for pos, val in grid.items() if val == 0)
