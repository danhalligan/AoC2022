from aoc2022.helpers import input_lines


def part1(file):
    return None


def part2(file):
    return None


# dat = input_lines("inputs/day02.txt")
dat = input_lines("tests/inputs/day02.txt")
dat = [x.split(" ") for x in dat]

score = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

sum([score[x] for x in dat])

dat = input_lines("inputs/day02.txt")
sum([score[x] for x in dat])


score2 = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}
dat = input_lines("tests/inputs/day02.txt")
sum([score2[x] for x in dat])

dat = input_lines("inputs/day02.txt")
sum([score2[x] for x in dat])
