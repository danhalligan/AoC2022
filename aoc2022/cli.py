import typer
import re
import importlib
import os
import requests
from pathlib import Path
from typing import List
from datetime import date

app = typer.Typer()


@app.command("solve")
def solve(files: List[Path]):
    """Solve a challenges based on filename"""
    for path in files:
        if path.is_file():
            day = int(re.findall(r"\d+", path.name)[0])
            print(f"--- Day {day} ---")
            module = importlib.import_module(f"aoc2022.day{day:02d}")
            try:
                print("Part 1:", getattr(module, "part1")(path))
            except AttributeError:
                print("No part 1")
            try:
                print("Part 2:", getattr(module, "part2")(path))
            except AttributeError:
                print("No part 2")
            print()


@app.command("input")
def input(day: int = date.today().day):
    """Download AoC input file (for today by default)"""
    print(f"Downloading https://adventofcode.com/2022/day/{day}/input")
    if "AOC_SESSION" not in os.environ and os.path.exists(".session.txt"):
        os.environ["AOC_SESSION"] = open(".session.txt").read().rstrip()
    res = requests.get(
        f"https://adventofcode.com/2022/day/{day}/input",
        cookies={"session": os.environ.get("AOC_SESSION")},
    )
    with open("inputs/day" + f"{day:02d}" + ".txt", "w") as f:
        f.write(res.text)
    return "inputs/day" + f"{day:02d}" + ".txt"


def main():
    app()
