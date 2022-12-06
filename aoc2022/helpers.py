# Functions to help read inputs
import re


def ints(x):
    """Coerce a list into a list of ints"""
    return [int(y) for y in x]


def input_str(file):
    """Returns input file as a str"""
    return open(file, "r").read().rstrip()


def input_lines(file):
    """Returns lines from input file"""
    return input_str(file).splitlines()


def input_ints(file):
    """Returns list of ints from input file (split by new line or comma)"""
    txt = input_str(file)
    return ints(re.split(r"[\n,]", txt))


def input_blocks(file, sep="\n\n"):
    """Returns lines of input split by empty lines from input file"""
    blocks = open(file).read().split(sep)
    return [block.split() for block in blocks]
