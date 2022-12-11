import re
from aoc2022.helpers import ints, getint
from math import prod


class Monkey:
    def __init__(self, dat):
        dat = dat.split("\n")
        self.items = ints(re.findall("-*\\d+", dat[1]))
        self.op = re.match(r".+new = (.+$)", dat[2]).groups(1)[0]
        self.test = getint(dat[3])
        self.true = getint(dat[4])
        self.false = getint(dat[5])
        self.inspected = 0

    def apply(self, old):
        return eval(self.op)


def round(monkeys, fn):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.pop(0)
            item = monkey.apply(item)
            item = fn(item)
            if item % monkey.test == 0:
                monkeys[monkey.true].items += [item]
            else:
                monkeys[monkey.false].items += [item]
            monkey.inspected += 1


def part1(file):
    monkeys = open(file).read().split("\n\n")
    monkeys = [Monkey(x) for x in monkeys]
    for _ in range(20):
        round(monkeys, lambda x: x // 3)
    insp = [x.inspected for x in monkeys]
    return prod(sorted(insp)[-2:])


# The logic here is that each monkey's test is checking for divisibility by a
# set of possible integers. We can get the same answer if we test for
# divisibility by that number modulo x, if x divisible by our test number. To
# ensure this is always true, we set x to be the product of the test numbers.
def part2(file):
    monkeys = open(file).read().split("\n\n")
    monkeys = [Monkey(x) for x in monkeys]
    mod_val = prod([x.test for x in monkeys])
    for _ in range(10000):
        round(monkeys, lambda x: x % mod_val)
    insp = [x.inspected for x in monkeys]
    return prod(sorted(insp)[-2:])
