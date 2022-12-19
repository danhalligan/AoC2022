from aoc2022.helpers import input_lines, ints
import re
from heapq import heappush, heappop
import math


def data(file):
    for line in input_lines(file):
        x = ints(re.findall(r"-*\d+", line))
        yield [
            [x[1], 0, 0, 0],
            [x[2], 0, 0, 0],
            [x[3], x[4], 0, 0],
            [x[5], 0, x[6], 0],
        ]


def available(resource, costs):
    for r in range(4):
        if all([resource[x] >= costs[r][x] for x in range(4)]):
            yield r


def build(robot, resource, costs):
    return tuple(
        [
            resource[0] - costs[robot][0],
            resource[1] - costs[robot][1],
            resource[2] - costs[robot][2],
            resource[3] - costs[robot][3],
        ]
    )


def add_resource(resource, robots):
    return tuple([resource[r] + robots[r] for r in range(4)])


def add_robot(robots, robot):
    robots = list(robots)
    robots[robot] += 1
    return tuple(robots)


def triangular(n):
    return n * (n + 1) // 2


def score(robots):
    return -sum(10 ** (i + 1) * j for i, j in enumerate(robots))


# NOTES:
# Since we can only build one robot each round, there's no point having more
# ore robots than the max ore required to build any robot (since they will
# generate enough ore each round).
def mine(costs, maxtime=24):
    maxc = [max(x) for x in zip(*costs)]
    q = []
    heappush(
        q, [score([1, 0, 0, 0]), [tuple([0, 0, 0, 0]), tuple([1, 0, 0, 0]), maxtime]]
    )
    best = 0
    seen = set()
    while q:
        sc, (resource, robots, time) = heappop(q)
        state = tuple(list(resource) + list(robots) + [time])
        if state in seen:
            continue
        if resource[3] + robots[3] * time + triangular(time) <= best:
            continue
        if time == 0:
            best = max(best, resource[3])
            continue
        seen.add(state)
        avail = set(available(resource, costs))
        resource = add_resource(resource, robots)
        for robot in avail:
            if robot == 3 or robots[robot] <= maxc[robot]:
                rsc = build(robot, resource, costs)
                rbts = add_robot(robots, robot)
                heappush(q, [score(rbts), [rsc, rbts, time - 1]])
        heappush(q, [score(robots), [resource, robots, time - 1]])
    return best


def part1(file):
    bests = []
    for costs in data(file):
        bests.append(mine(costs))
    return sum([x * (i + 1) for i, x in enumerate(bests)])


def part2(file):
    bests = []
    for costs in list(data(file))[:3]:
        bests.append(mine(costs, maxtime=32))
    return math.prod(bests)
