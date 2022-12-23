import re


def data(file):
    grid, moves = open(file).read().split("\n\n")
    board = {}
    for j, row in enumerate(grid.split("\n")):
        for i, x in enumerate(list(row)):
            board[j, i] = x
    return board, moves


def nextp(pos, facing, board):
    if facing == 0:
        maxc = max(k[1] for k in board.keys() if k[0] == pos[0]) + 1
        return (pos[0], (pos[1] + 1) % maxc)
    elif facing == 1:
        maxr = max(k[0] for k in board.keys() if k[1] == pos[1]) + 1
        return ((pos[0] + 1) % maxr, pos[1])
    elif facing == 2:
        maxc = max(k[1] for k in board.keys() if k[0] == pos[0]) + 1
        return (pos[0], (pos[1] - 1) % maxc)
    else:
        maxr = max(k[0] for k in board.keys() if k[1] == pos[1]) + 1
        return ((pos[0] - 1) % maxr, pos[1])


def turn(facing, rotation):
    if rotation == "R":
        return (facing + 1) % 4
    else:
        return (facing - 1) % 4


def data2(file):
    board, moves = data(file)
    A = {
        (k[0], k[1] - 50): v
        for k, v in board.items()
        if k[0] < 50 and k[1] >= 50 and k[1] < 100
    }
    B = {(k[0], k[1] - 100): v for k, v in board.items() if k[0] < 50 and k[1] >= 100}
    C = {
        (k[0] - 50, k[1] - 50): v
        for k, v in board.items()
        if k[0] >= 50 and k[0] < 100 and k[1] >= 50
    }
    D = {
        (k[0] - 100, k[1]): v
        for k, v in board.items()
        if k[0] >= 100 and k[0] < 150 and k[1] < 50
    }
    E = {
        (k[0] - 100, k[1] - 50): v
        for k, v in board.items()
        if k[0] >= 100 and k[0] < 150 and k[1] >= 50
    }
    F = {(k[0] - 150, k[1]): v for k, v in board.items() if k[0] >= 150}
    return {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F}, moves


# position is row then column
# Facing is 0:right 1:down, 2:left, 3:up
def part1(file):
    board, moves = data(file)
    pos = (0, min(k[1] for k in board.keys() if k[0] == 0 and board[k] == "."))
    facing = 0
    moves = re.findall(r"\d+[RL]*", moves)
    moves[-1] = moves[-1] + "."  # horrible hack!

    for move in moves:
        dist, rotation = int(move[:-1]), move[-1]

        for _ in range(dist):
            new = nextp(pos, facing, board)
            while board[new] == " ":
                new = nextp(new, facing, board)
            if board[new] == "#":
                break
            pos = new

        if rotation in ["L", "R"]:
            facing = turn(facing, rotation)
        # print(pos)

    return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing


# My input looks as follows:
#  AB
#  C
# DE
# F
#
# Tiles are 50x50

# How to move off the end of a tile
# (row, column)
# 0:right 1:down, 2:left, 3:up
def tile_move(tile, p, facing):
    m = {
        ("A", 0): ["B", (p[0], 0), 0],
        ("A", 1): ["C", (0, p[1]), 1],
        ("A", 2): ["D", (49 - p[0], 0), 0],
        ("A", 3): ["F", (p[1], 0), 0],
        ("B", 0): ["E", (49 - p[0], 49), 2],
        ("B", 1): ["C", (p[1], 49), 2],
        ("B", 2): ["A", (p[0], 49), 2],
        ("B", 3): ["F", (49, p[1]), 3],
        ("C", 0): ["B", (49, p[0]), 3],
        ("C", 1): ["E", (0, p[1]), 1],
        ("C", 2): ["D", (0, p[0]), 1],
        ("C", 3): ["A", (49, p[1]), 3],
        ("D", 0): ["E", (p[0], 0), 0],
        ("D", 1): ["F", (0, p[1]), 1],
        ("D", 2): ["A", (49 - p[0], 0), 0],
        ("D", 3): ["C", (p[1], 0), 0],
        ("E", 0): ["B", (49 - p[0], 49), 2],
        ("E", 1): ["F", (p[1], 49), 2],
        ("E", 2): ["D", (p[0], 49), 2],
        ("E", 3): ["C", (49, p[1]), 3],
        ("F", 0): ["E", (49, p[0]), 3],
        ("F", 1): ["B", (0, p[1]), 1],
        ("F", 2): ["A", (0, p[0]), 1],
        ("F", 3): ["D", (49, p[1]), 3],
    }
    return m[tile, facing]


def nextp2(tile, pos, facing):
    if facing == 0:
        new = (pos[0], pos[1] + 1)
        if new[1] > 49:
            return tile_move(tile, pos, facing)
    elif facing == 1:
        new = (pos[0] + 1, pos[1])
        if new[0] > 49:
            return tile_move(tile, pos, facing)
    elif facing == 2:
        new = (pos[0], pos[1] - 1)
        if new[1] < 0:
            return tile_move(tile, pos, facing)
    else:
        new = (pos[0] - 1, pos[1])
        if new[0] < 0:
            return tile_move(tile, pos, facing)
    return tile, new, facing


# My input looks as follows:
#  AB
#  C
# DE
# F
def tile2coord(tile, pos):
    if tile == "A":
        return (pos[0], pos[1] + 50)
    if tile == "B":
        return (pos[0], pos[1] + 100)
    if tile == "C":
        return (pos[0] + 50, pos[1] + 50)
    if tile == "D":
        return (pos[0] + 100, pos[1])
    if tile == "E":
        return (pos[0] + 100, pos[1] + 50)
    if tile == "F":
        return (pos[0] + 150, pos[1])


def part2(file):
    tiles, moves = data2(file)
    moves = re.findall(r"\d+[RL]*", moves)
    moves[-1] = moves[-1] + "."  # horrible hack!
    tile = "A"
    pos = (0, 0)
    facing = 0
    for move in moves:
        dist, rotation = int(move[:-1]), move[-1]
        for _ in range(dist):
            ntile, npos, nfacing = nextp2(tile, pos, facing)
            if tiles[ntile][npos] == "#":
                break
            tile, pos, facing = ntile, npos, nfacing
        if rotation in ["L", "R"]:
            facing = turn(facing, rotation)

    pos = tile2coord(tile, pos)
    return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing
