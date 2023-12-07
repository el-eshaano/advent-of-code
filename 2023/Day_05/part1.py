import readfile

inputs = readfile.seperated_by_newlines('input.txt')
seeds = [int(x) for x in inputs[0].split(' ') if x.isdigit()]

print(seeds)

maps = []
for map in inputs[1:]:

    d = []

    map = map.split("\n")
    map_name, map_data = map[:1], map[1:]
    for data in map_data:
        d.append([int(x) for x in data.split(' ')])

    maps.append(d)

min_dist = float('inf')
for s in seeds:
    for map in maps:
        for _range in map:
            dest_start, src_start, range_len = _range
            if src_start <= s < src_start + range_len:
                s = dest_start + (s - src_start)
                break

    if s < min_dist:
        min_dist = s

print(min_dist)
