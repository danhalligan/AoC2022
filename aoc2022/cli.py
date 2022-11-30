import typer
import re
import importlib
from pathlib import Path
from typing import List
from aoc2022.helpers import get_input

app = typer.Typer()


@app.command("solve")
def solve(files: List[Path]):
    """Solve a challenges based on filename"""
    for path in files:
        if path.is_file():
            day = int(re.findall(r"\d+", path.name)[0])
            print(f"--- Day {day} ---")
            module = importlib.import_module(f"aoc2022.day{day:02d}")
            print("Part 1:", getattr(module, "part1")(path))
            try:
                print("Part 2:", getattr(module, "part2")(path))
            except AttributeError:
                print("No part 2")
            print()


@app.command("input")
def input():
    get_input()


def main():
    app()
