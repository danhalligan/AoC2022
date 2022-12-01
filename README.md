# AoC2022

![CI workflow](https://github.com/danhalligan/AoC2022/actions/workflows/ci.yaml/badge.svg)
![License](https://img.shields.io/github/license/danhalligan/AoC2022)
![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)

`AoC2022` is a python package implementing solutions python solutions for the
[Advent of Code 2022] problems.

## Example

To download input data for today's day run:

``` bash
poetry run aoc2022 input
```

To solve a specific day, you can use `solve`, passing in the input file for
the current day using poetry.

``` bash
poetry run aoc2022 solve inputs/day01.txt
```

Or pass in multiple days to solve multiple inputs.

``` bash
poetry run aoc2022 solve inputs/*
```

You can automatically download the input for a given day by setting your
[session cookie] in an environment variable (or in a `.session.txt` text file
in the working directory).

``` bash
export AOC_SESSION=[your session]
```

Then using the helper function, e.g. for today's input:

```python
> from aoc2022.helpers import *
> get_input()
```

[Advent of Code 2022]: https://adventofcode.com/2022
[session cookie]: https://www.reddit.com/r/adventofcode/comments/a2vonl/how_to_download_inputs_with_a_script/
