from aoc2022.helpers import input_lines
from operator import add, sub, mul, floordiv, eq
from copy import copy

op = {"+": add, "-": sub, "*": mul, "/": floordiv, "=": eq}


def data(file):
    lines = input_lines(file)
    g = {}
    k = {}
    for line in lines:
        name, p = line.split(": ")
        p = p.split(" ")
        if len(p) == 1:
            k[name] = int(p[0])
        else:
            g[name] = p
    return k, g


def solve(k, g):
    while g:
        for n, x in list(g.items()):
            if x[0] in k.keys() and x[2] in k.keys():
                k[n] = op[x[1]](k[x[0]], k[x[2]])
                del g[n]
    return k["root"]


def part1(file):
    k, g = data(file)
    return solve(k, g)


# Set humn to n and evaluate, returning difference of inputs for root
def testn(n, g, k):
    g = copy(g)
    k = copy(k)
    k["humn"] = n
    return solve(k, g)


# binary search
def part2(file):
    k, g = data(file)
    g["root"][1] = "-"
    low = 1
    high = 10000000000000
    while True:
        mid = (low + high) // 2
        res = testn(mid, g, k)
        if res == 0 or high == low + 1:
            break
        elif res > 0:
            low = mid
        else:
            high = mid
    return mid
