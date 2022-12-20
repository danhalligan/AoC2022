from collections import deque
from aoc2022.helpers import input_ints

# There are duplicates, so we need to make each unique!


def grove(x):
    x = deque(x)
    x.rotate(-x.index(0))
    pos = [1000 % len(x), 2000 % len(x), 3000 % len(x)]
    return sum(x[i] for i in pos)


def mix(x, d):
    for i in x:
        d.rotate(-d.index(i))
        o = d.popleft()
        d.rotate(-o[1])
        d.insert(0, o)


def part1(file):
    x = list(enumerate(input_ints(file)))
    d = deque(x)
    mix(x, d)
    return grove([n[1] for n in d])


def part2(file):
    x = list(enumerate(input_ints(file)))
    x = [(n[0], n[1] * 811589153) for n in x]
    d = deque(x)

    for _ in range(10):
        mix(x, d)

    return grove([n[1] for n in d])
