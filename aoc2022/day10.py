from aoc2022.helpers import input_lines
from advent_of_code_ocr import convert_array_6


def part1(file):
    program = input_lines(file)
    X = 1
    i = 0
    count = 2
    cycle = 1
    strength = []
    while i < len(program):
        if (cycle - 20) % 40 == 0:
            strength += [cycle * X]
        if program[i] == "noop":
            i += 1
        elif program[i].startswith("addx"):
            count -= 1
            if count == 0:
                X += int(program[i].split(" ")[1])
                count = 2
                i += 1
        cycle += 1
    return sum(strength)


def part2(file):
    program = input_lines(file)
    X = 1
    i = 0
    count = 2
    cycle = 1
    screen = [["."] * 40 for i in range(6)]
    while i < len(program):
        sprite = [X - 1, X, X + 1]
        if (cycle - 1) % 40 in sprite:
            row = (cycle - 1) // 40
            col = (cycle - 1) % 40
            screen[row][col] = "#"
        if program[i] == "noop":
            i += 1
        elif program[i].startswith("addx"):
            count -= 1
            if count == 0:
                X += int(program[i].split(" ")[1])
                count = 2
                i += 1
        cycle += 1
    try:
        return convert_array_6(screen)
    except KeyError:
        return None
