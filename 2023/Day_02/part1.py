import readfile
from collections import defaultdict

FILENAME = 'input.txt'
inputs = readfile.line_by_line(FILENAME)

sum = 0
for gID, g in enumerate(inputs):
    possible = True
    for s in g.split(':')[1].split(";"):
        counts = defaultdict(int)
        for t in s.split(", "):
            t = t.strip()
            count, colour = t.split(" ")[0], t.split(" ")[1]
            counts[colour] += int(count)
        if not (counts["red"] <= 12 and counts["green"] <= 13 and counts["blue"] <= 14):
            possible = False

    if possible:
        sum += gID + 1

print(sum)
