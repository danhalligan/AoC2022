from collections import defaultdict


class Shape:
    def __init__(self, x):
        self.shape = x
        self.pos = [0, 0]

    def width(self):
        return len(self.shape[0])

    def height(self):
        return len(self.shape)

    def __repr__(self):
        rows = ["".join("#" if x else "." for x in row) for row in self.shape]
        return "\n".join(rows[::-1]) + "\n"

    def ledge(self):
        return [x[0] for x in self.shape]

    def redge(self):
        return [x[self.width() - 1] for x in self.shape]

    def bedge(self):
        return self.shape[0]

    def lshift(self, cave, debug=False):
        if debug:
            breakpoint()
        if self.pos[0] == 0:
            return False
        edge = self.ledge()
        for pos in range(self.height()):
            row = pos + self.pos[1]
            col = self.pos[0]
            if cave.cave[row, col - 1] and edge[pos] == 1:
                return False
            elif edge[pos] == 0 and cave.cave[row, col]:
                return False
        self.pos[0] -= 1
        return True

    def rshift(self, cave, debug=False):
        if debug:
            breakpoint()
        if self.pos[0] == 7 - self.width():
            return False
        edge = self.redge()
        for pos in range(self.height()):
            row = pos + self.pos[1]
            col = self.pos[0] + self.width() - 1
            if cave.cave[row, col + 1] and edge[pos]:
                return False
            elif edge[pos] == 0 and cave.cave[row, col]:
                return False
        self.pos[0] += 1
        return True

    def shift(self, cave, d, debug=False):
        if d == -1:
            return self.lshift(cave, debug=debug)
        else:
            return self.rshift(cave, debug=debug)

    def drop(self, cave, debug=False):
        if debug:
            breakpoint()
        if self.pos[1] == 0:
            return False
        edge = self.bedge()
        row = self.pos[1]
        for pos in range(self.width()):
            col = self.pos[0] + pos
            if cave.cave[row - 1, col] and edge[pos]:
                return False
            elif edge[pos] == 0 and cave.cave[row, col]:
                return False
        self.pos[1] -= 1
        return True

    def move(self, cave, jets):
        while True:
            self.shift(cave, jets.__next__())
            res = self.drop(cave)
            if not res:
                return


class Cave:
    def __init__(self):
        self.cave = defaultdict(bool)

    def print(self, shape):
        if shape:
            top = shape.pos[1] + shape.height()
        else:
            top = self.top()
        for r in range(top, -1, -1):
            row = ""
            for c in range(7):
                if (
                    shape
                    and r >= shape.pos[1]
                    and r < shape.pos[1] + shape.height()
                    and c >= shape.pos[0]
                    and c < shape.pos[0] + shape.width()
                    and shape.shape[r - shape.pos[1]][c - shape.pos[0]]
                ):
                    row += "@"
                elif self.cave[r, c]:
                    row += "#"
                else:
                    row += "."
            print("|" + row + "|")
        print("---------")

    def alter(self, shape):
        for row in range(shape.width()):
            for col in range(shape.height()):
                if shape.shape[col][row]:
                    self.cave[col + shape.pos[1], row + shape.pos[0]] = True

    def top(self):
        vals = [x[0] for x, v in self.cave.items() if v]
        if len(vals):
            return max(vals)
        else:
            return -1
