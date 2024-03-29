import re
import sys
from collections import Counter, defaultdict, deque
from copy import deepcopy
from math import gcd

with open("day13.in") as file:
    data = file.read().strip()
    L = data.split("\n")

# print(data)
# print(L)

G = [[c for c in row] for row in L]

for part2 in [False, True]:
    ans = 0
    for grid in data.split("\n\n"):
        G = [[c for c in row] for row in grid.split("\n")]
        R = len(G)
        C = len(G[0])
        # vertical symmetry
        for c in range(C - 1):
            badness = 0
            for dc in range(C):
                left = c - dc
                right = c + 1 + dc
                if 0 <= left < right < C:
                    for r in range(R):
                        if G[r][left] != G[r][right]:
                            badness += 1
            if badness == (1 if part2 else 0):
                ans += c + 1
        for r in range(R - 1):
            badness = 0
            for dr in range(R):
                up = r - dr
                down = r + 1 + dr
                if 0 <= up < down < R:
                    for c in range(C):
                        if G[up][c] != G[down][c]:
                            badness += 1
            if badness == (1 if part2 else 0):
                ans += 100 * (r + 1)
    print(ans)
