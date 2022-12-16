import re
from aoc2022.helpers import input_lines
from functools import cache


def data(file):
    g, flow = {}, {}
    for line in input_lines(file):
        valve, rate, to = re.match(
            r"Valve (\w+) has flow rate=(\d+); tunnel[s]* lead[s]* to valve[s]* (.+$)",
            line,
        ).groups()
        g[valve] = to.split(", ")
        flow[valve] = int(rate)
    return g, flow


def part1(file):
    @cache
    def maxflow(opened, time, curr):
        if time <= 0:
            return 0
        best = 0
        for valve in g[curr]:
            # move to next room
            best = max(best, maxflow(opened, time - 1, valve))
        if curr not in opened and flow[curr] > 0 and time > 0:
            # open valve, then move
            opened = set(opened)
            opened.add(curr)
            for valve in g[curr]:
                res = maxflow(frozenset(opened), time - 2, valve)
                best = max(best, (time - 1) * flow[curr] + res)
        return best

    g, flow = data(file)
    return maxflow(frozenset(), 30, "AA")


def part2(file):
    @cache
    def maxflow(opened, time, curr, run):
        if time <= 0:
            if run == 1:
                return maxflow(opened, 26, "AA", 2)
            else:
                return 0
        best = 0
        for valve in g[curr]:
            best = max(best, maxflow(opened, time - 1, valve, run))
        if curr not in opened and flow[curr] > 0 and time > 0:
            opened = set(opened)
            opened.add(curr)
            for valve in g[curr]:
                res = maxflow(frozenset(opened), time - 2, valve, run)
                best = max(best, (time - 1) * flow[curr] + res)
        return best

    g, flow = data(file)
    return maxflow(frozenset(), 26, "AA", 1)
