from aoc2022.helpers import input_lines
import re


def parse(file):
    dat = input_lines(file)
    files = {"/": {"f": {}, "d": [], "p": None}}
    dirs = []
    pos = 1
    curr = "/"
    while pos < len(dat):
        if dat[pos] == "$ ls":
            pos += 1
            while pos < len(dat) and re.match(r"^[^\$]", dat[pos]):
                if re.match(r"^\d+", dat[pos]):
                    size, n = dat[pos].split()
                    files[curr]["f"][n] = int(size)
                elif re.match(r"^dir", dat[pos]):
                    _, n = dat[pos].split()
                    files[curr]["d"] += [f"{curr}/{n}"]
                    dirs += [f"{curr}/{n}"]
                pos += 1
        elif dat[pos] == "$ cd ..":
            curr = files[curr]["p"]
            pos += 1
        elif re.match(r"^\$ cd", dat[pos]):
            _, _, n = dat[pos].split()
            files[f"{curr}/{n}"] = {"f": {}, "d": [], "p": None}
            files[f"{curr}/{n}"]["p"] = curr
            curr = f"{curr}/{n}"
            pos += 1
    return files, dirs


# recursively sum directories
def dirsize(files, name):
    s1 = sum(x for x in files[name]["f"].values())
    s2 = sum(dirsize(files, n) for n in files[name]["d"])
    return s1 + s2


def part1(file):
    files, dirs = parse(file)
    sizes = {n: dirsize(files, n) for n in ["/"] + dirs}
    return sum(s for x, s in sizes.items() if s <= 100000)


def part2(file):
    files, dirs = parse(file)
    sizes = {n: dirsize(files, n) for n in ["/"] + dirs}
    unused = 70000000 - sizes["/"]
    to_free = 30000000 - unused
    return min(s for x, s in sizes.items() if s >= to_free)
