from functools import cmp_to_key


def enlist(x):
    if not isinstance(x, list):
        return [x]
    else:
        return x


def ordered(left, right):
    i = 0
    while True:
        if i >= len(left):
            return True
        if i >= len(right):
            return False
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return True
            if left[i] > right[i]:
                return False
        else:
            res = ordered(enlist(left[i]), enlist(right[i]))
            if res is not None:
                return res
        i += 1


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
