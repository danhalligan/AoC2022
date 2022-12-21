from aoc2022.helpers import input_lines
from operator import add, sub, mul, truediv, eq
from copy import copy

op = {"+": add, "-": sub, "*": mul, "/": truediv, "=": eq}


def sign(x):
    return -1 if x < 0 else (1 if x > 0 else 0)


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
    return int(solve(k, g))


# Set humn to n and evaluate, returning difference of inputs for root
def testn(n, g, k):
    g = copy(g)
    k = copy(k)
    k["humn"] = n
    g["root"][1] = "-"
    return solve(k, g)


# binary search
def part2(file):
    k, g = data(file)
    low = 1
    high = 100000000000000
    res = {}
    res[low] = testn(low, g, k)
    res[high] = testn(high, g, k)
    while True:
        mid = (low + high) // 2
        res[mid] = testn(mid, g, k)
        if res[mid] == 0.0 or high == low + 1:
            break
        elif sign(res[mid]) == sign(res[low]):
            low = mid
        else:
            high = mid
    return mid
