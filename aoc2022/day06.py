def data(file):
    return open(file).read().rstrip()


def marker(dat, size):
    for i in range(len(dat) - size + 1):
        if len(set(dat[i : i + size])) == size:
            break
    return i + size


def part1(file):
    return marker(data(file), 4)


def part2(file):
    return marker(data(file), 14)
