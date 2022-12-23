from collections import defaultdict


# 8 surrounding positions
def n1(p):
    return [
        (p[0] - 1, p[1] - 1),
        (p[0], p[1] - 1),
        (p[0] + 1, p[1] - 1),
        (p[0] - 1, p[1]),
        (p[0] + 1, p[1]),
        (p[0] - 1, p[1] + 1),
        (p[0], p[1] + 1),
        (p[0] + 1, p[1] + 1),
    ]


# [N, NE, NW], [S, SE, SW], [W, NW, SW], [E, NE, SE]
def n2(p):
    return [
        [(p[0] - 1, p[1] - 1), (p[0] - 1, p[1]), (p[0] - 1, p[1] + 1)],
        [(p[0] + 1, p[1] - 1), (p[0] + 1, p[1]), (p[0] + 1, p[1] + 1)],
        [(p[0] - 1, p[1] - 1), (p[0], p[1] - 1), (p[0] + 1, p[1] - 1)],
        [(p[0] - 1, p[1] + 1), (p[0], p[1] + 1), (p[0] + 1, p[1] + 1)],
    ]


# [N, S, W, E]
def n3(p):
    return [(p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)]


def data(file):
    board = defaultdict(lambda: ".")
    for j, row in enumerate(open(file).read().split("\n")):
        for i, x in enumerate(list(row)):
            board[j, i] = x
    return board


def printb(board):
    c = [p[0] for p in board.keys()]
    r = [p[1] for p in board.keys()]
    for j in range(min(c), max(c) + 1):
        print(*[board[j, i] for i in range(min(r), max(r) + 1)], sep="")


def rotate(x, n):
    return x[n % 4 :] + x[: n % 4]


def propose(board, rnd):
    proposal = {}
    for pos, val in list(board.items()):
        if val == "#":
            if any(board[p] == "#" for p in n1(pos)):
                prop = [any(board[p] == "#" for p in x) for x in n2(pos)]
                if not all(prop):
                    prop = rotate(prop, rnd)
                    proposal[pos] = rotate(n3(pos), rnd)[prop.index(False)]
    return proposal


def move(board, proposal):
    for pos, val in board.items():
        if val == "#" and pos in proposal:
            if list(proposal.values()).count(proposal[pos]) == 1:
                board[pos] = "."
                board[proposal[pos]] = "#"


def empties(board):
    c = [p[0] for p in board.keys() if board[p] == "#"]
    r = [p[1] for p in board.keys() if board[p] == "#"]
    tot = 0
    for j in range(min(c), max(c) + 1):
        tot += sum(board[j, i] == "." for i in range(min(r), max(r) + 1))
    return tot


def part1(file):
    board = data(file)

    rnd = 0
    while True:
        proposal = propose(board, rnd)
        if not proposal or rnd == 10:
            break
        move(board, proposal)
        rnd += 1

    return empties(board)


def part2(file):
    board = data(file)

    rnd = 0
    while True:
        proposal = propose(board, rnd)
        if not proposal:
            break
        move(board, proposal)
        rnd += 1

    return rnd + 1
