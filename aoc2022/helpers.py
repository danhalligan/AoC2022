# Functions to help read inputs
import re
import os
import requests
from datetime import date


def input_str(file):
    """Returns input file as a str"""
    return open(file, "r").read()


def input_lines(file):
    """Returns lines from input file"""
    return input_str(file).splitlines()


def input_ints(file):
    """Returns list of ints from input file"""
    txt = input_str(file).rstrip()
    return list(map(int, re.split(r"[\n,]", txt)))


def input_blocks(file):
    """Returns lines of input split by empty lines from input file"""
    blocks = open(file).read().split("\n\n")
    return [block.split() for block in blocks]


def get_input(day=date.today().day):
    print(f"Downloading https://adventofcode.com/2022/day/{day}/input")
    if not "AOC_SESSION" in os.environ and os.path.exists(".session.txt"):
        os.environ["AOC_SESSION"] = open(".session.txt").read().rstrip()
    res = requests.get(
        f"https://adventofcode.com/2022/day/{day}/input",
        cookies={"session": os.environ.get("AOC_SESSION")},
    )
    with open("inputs/day" + f"{day:02d}" + ".txt", "w") as f:
        f.write(res.text)
    return "inputs/day" + f"{day:02d}" + ".txt"
