import readfile

input = readfile.as_2D_grid('input.txt')


def get_neighbours(r, c, grid):
    n = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= r+i < len(grid) and 0 <= c+j < len(grid[0]):
                n.append((r+i, c+j, grid[r+i][c+j]))

    return n


def get_number(r, c, grid):
    start, end = c, c
    while start > 0 and grid[r][start-1].isdigit():
        start -= 1
    while end < len(grid[0]) and grid[r][end].isdigit():
        end += 1

    return int("".join(grid[r][start:end]))


seen_numbers = set()
for i, row in enumerate(input):
    for j, c in enumerate(row):
        if c.isdigit() or c == ".":
            continue

        for r, c, val in get_neighbours(i, j, input):
            if val.isdigit():
                seen_numbers.add(get_number(r, c, input))

print(sum(list(seen_numbers)))
