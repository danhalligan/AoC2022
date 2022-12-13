from copy import copy
from functools import cmp_to_key


def ordered(left, right):
    left, right = copy(left), copy(right)
    while left or right:
        try:
            l2 = left.pop(0)
        except IndexError:
            return True
        try:
            r2 = right.pop(0)
        except IndexError:
            return False
        if isinstance(l2, int) and isinstance(r2, int):
            if l2 < r2:
                return True
            if l2 > r2:
                return False
            continue
        elif isinstance(l2, int):
            l2 = [l2]
        elif isinstance(r2, int):
            r2 = [r2]
        if isinstance(l2, list) and isinstance(r2, list):
            v = ordered(l2, r2)
            if v is not None:
                return v


def data(file):
    blocks = open(file).read().split("\n\n")
    return [[eval(y) for y in x.rstrip().split("\n")] for x in blocks]


def part1(file):
    packets = data(file)
    return sum(i + 1 for i, x in enumerate(packets) if ordered(*x))


def part2(file):
    all_packets = [x for y in data(file) for x in y] + [[[2]]] + [[[6]]]
    all_packets = sorted(
        all_packets, key=cmp_to_key(lambda x, y: -1 if ordered(x, y) else 1)
    )
    return (all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1)
