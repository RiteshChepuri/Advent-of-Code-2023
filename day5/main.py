from collections import defaultdict

with open("day5.in") as file:
    data = file.read().strip()

# print(data)

L = data.split("\n")

# print(L)

parts = data.split("\n\n")
seed, *others = parts
seed = [int(x) for x in seed.split(":")[1].split()]


class Function:
    def __init__(self, S):
        lines = S.split("\n")[1:]
        self.tuples: list[tuple[int, int, int]] = [
            [int(x) for x in line.split()] for line in lines
        ]
        # print(self.tuples)

    def apply_one(self, x: int) -> int:
        for dst, src, sz in self.tuples:
            if src <= x < src + sz:
                return x + dst - src
        return x

    def apply_range(self, R):
        A = []
        for dest, src, sz in self.tuples:
            src_end = src + sz
            NR = []
            while R:
                (st, ed) = R.pop()
                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0]:
                    NR.append(before)
                if inter[1] > inter[0]:
                    A.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    NR.append(after)
            R = NR
        return A + R


Fs = [Function(s) for s in others]


def f(R, o):
    A = []
    for line in o:
        dest, src, sz = [int(x) for x in line.split()]
        src_end = src + sz


P1 = []
for x in seed:
    for a in Fs:
        x = a.apply_one(x)
    P1.append(x)
print(min(P1))

P2 = []
pairs = list(zip(seed[::2], seed[1::2]))
for st, sz in pairs:
    R = [(st, st + sz)]
    for a in Fs:
        R = a.apply_range(R)
    # print(len(R))
    P2.append(min(R)[0])
print(min(P2))
