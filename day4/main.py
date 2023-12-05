from collections import defaultdict


with open("day4.in") as file:
    data = file.read().strip()

# print(data)

lines = data.split("\n")

# print(lines)

p1 = 0
P = defaultdict(int)

for i, line in enumerate(lines):
    P[i] += 1
    first, rest = line.split("|")
    Id, card = first.split(":")
    card_num = [int(x) for x in card.split()]
    rest_num = [int(x) for x in rest.split()]
    val = len(set(card_num) & set(rest_num))
    if val > 0:
        p1 += 2 ** (val - 1)
    for j in range(val):
        P[i + 1 + j] += P[i]
print(p1)
print(sum(P.values()))
