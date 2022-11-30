# Functions to help read inputs
import re
import os
import requests
from datetime import date


def input_str(file):
    return open(file, "r").read()


def input_lines(file):
    return input_str(file).splitlines()


def input_ints(file):
    txt = input_str(file).rstrip()
    return list(map(int, re.split(r"[\n,]", txt)))


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
