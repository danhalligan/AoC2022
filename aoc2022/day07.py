from aoc2022.helpers import input_lines


def path(tree):
    return "/".join(tree)


def parse(file):
    dat = input_lines(file)
    files = {"/": {"f": {}, "d": []}}
    i = 1
    tree = ["/"]
    while i < len(dat):
        if dat[i] == "$ ls":
            i += 1
            while i < len(dat) and not dat[i].startswith("$"):
                if dat[i].startswith("dir"):
                    n = dat[i].split()[1]
                    files[path(tree)]["d"] += [path(tree + [n])]
                else:
                    size, n = dat[i].split()
                    files[path(tree)]["f"][n] = int(size)
                i += 1
        elif dat[i] == "$ cd ..":
            tree = tree[:-1]
            i += 1
        else:
            tree += [dat[i].split()[2]]
            files[path(tree)] = {"f": {}, "d": []}
            i += 1
    return files


def dirsize(files, name):
    s1 = sum(x for x in files[name]["f"].values())
    s2 = sum(dirsize(files, n) for n in files[name]["d"])
    return s1 + s2


def part1(file):
    files = parse(file)
    sizes = {n: dirsize(files, n) for n in files.keys()}
    return sum(s for x, s in sizes.items() if s <= 100000)


def part2(file):
    files = parse(file)
    sizes = {n: dirsize(files, n) for n in files.keys()}
    to_free = 30000000 - (70000000 - sizes["/"])
    return min(s for x, s in sizes.items() if s >= to_free)
