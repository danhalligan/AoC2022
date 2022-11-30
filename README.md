# AoC2022

`AoC2022` is a python package implementing solutions python solutions for the
[Advent of Code 2022] problems.

## Example

To solve a specific day, you can use `solve`, passing in the input file for
the current day using poetry.

``` bash
poetry run aoc2022 inputs/day01.txt
```

Or pass in multiple days to solve multiple inputs.

``` bash
poetry run aoc2022 inputs/*
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
