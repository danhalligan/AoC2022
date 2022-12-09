from aoc2022.helpers import input_lines
from collections import defaultdict


def move_head(pos, dir):
    if dir == "R":
        return (pos[0] + 1, pos[1])
    if dir == "L":
        return (pos[0] - 1, pos[1])
    if dir == "U":
        return (pos[0], pos[1] + 1)
    if dir == "D":
        return (pos[0], pos[1] - 1)


def touching(head, tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1


def step(a, b):
    return b if a == b else b + 1 if a > b else b - 1


def move_tail(head, tail):
    if touching(head, tail):
        return tail
    else:
        return (step(head[0], tail[0]), step(head[1], tail[1]))


def data(file):
    moves = input_lines(file)
    moves = [x.split(" ") for x in moves]
    return [[x, int(y)] for x, y in moves]


def part1(file):
    visited = defaultdict()
    rope = [(0, 0), (0, 0)]

    for move in data(file):
        for i in range(move[1]):
            rope[0] = move_head(rope[0], move[0])
            rope[1] = move_tail(rope[0], rope[1])
            visited[rope[1]] = True

    return len(visited)


def part2(file):
    visited = defaultdict()
    rope = [(0, 0)] * 10

    for move in data(file):
        for i in range(move[1]):
            rope[0] = move_head(rope[0], move[0])
            for j in range(9):
                rope[j + 1] = move_tail(rope[j], rope[j + 1])
            visited[rope[8]] = True

    return len(visited)
