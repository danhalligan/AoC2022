from aoc2022.helpers import input_lines, ints
import re


def merge_ranges(ranges):
    ranges.sort()
    stack = []
    stack.append(ranges[0])
    for i in ranges[1:]:
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
    return stack


def md(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


# for part each sensor, let's find coordinate ranges of coverage that
# overlap our row of interest
def find_ranges(coverage, row):
    ranges = []
    for sensor, cov in coverage:
        if sensor[1] <= row and sensor[1] + cov > row:
            # print(sensor)
            overlap = cov - (row - sensor[1])
            ranges += [[sensor[0] - overlap, sensor[0] + overlap]]
        if sensor[1] >= row and sensor[1] - cov < row:
            # print(sensor)
            overlap = cov - (sensor[1] - row)
            ranges += [[sensor[0] - overlap, sensor[0] + overlap]]
    return ranges


# We can determine the coverage of a sensor, based on its distance to
# the nearest beacon.
def data(file):
    coverage = []
    for line in input_lines(file):
        x = ints(re.findall(r"-*\d+", line))
        coverage += [[(x[0], x[1]), md(*x)]]
    return coverage


def part1(file, row=2000000):
    coverage = data(file)
    return sum(x[1] - x[0] for x in merge_ranges(find_ranges(coverage, row)))


def part2(file, n=4000000):
    coverage = data(file)
    for i in range(n):
        r = find_ranges(coverage, i)
        mr = merge_ranges([[x[0], x[1] + 1] for x in r])
        if len(mr) > 1:
            return mr[0][1] * 4000000 + i
