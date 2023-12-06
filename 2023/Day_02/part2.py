import readfile
from math import prod
from collections import defaultdict

inputs = readfile.line_by_line('input.txt')

sum = 0
for gID, g in enumerate(inputs):
    possible = True
    maxCounts = defaultdict(int)
    for s in g.split(':')[1].split(";"):
        for t in s.split(", "):

            t = t.strip()
            count, colour = t.split(" ")[0], t.split(" ")[1]

            if int(count) > maxCounts[colour]:
                maxCounts[colour] = int(count)

    sum += prod(maxCounts.values())

print(sum)
