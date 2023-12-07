import readfile

inputs = readfile.seperated_by_newlines('input.txt')
seed_ranges = [int(x) for x in inputs[0].split(' ') if x.isdigit()]
seed_ranges = [(seed_ranges[2*i], seed_ranges[2*i] + seed_ranges[2*i + 1])
               for i in range(len(seed_ranges)//2)]

maps = []
for map in inputs[1:]:

    d = []

    map = map.split("\n")
    map_name, map_data = map[:1], map[1:]
    for data in map_data:
        d.append([int(x) for x in data.split(' ')])

    maps.append(d)

final_ranges = seed_ranges
for map in maps:
    new_ranges = []
    for _range in final_ranges:
        intersection_ranges_found = []
        for dest, src, l in map:
            map_range = (src, src + l)
            if map_range[0] >= _range[1] or _range[0] >= map_range[1]:
                # No intersection between new_ranges
                continue
            else:
                # Intersection between ranges exists
                intersection_range = (
                    max(_range[0], map_range[0]), min(_range[1], map_range[1]))
                mapped_intersection_range = (
                    dest + intersection_range[0] - src, dest + intersection_range[1] - src)
                new_ranges.append(mapped_intersection_range)
                intersection_ranges_found.append(intersection_range)

        if intersection_ranges_found == []:
            new_ranges.append((_range[0], _range[1]))
        else:
            intersection_ranges_found.sort(key=lambda x: x[0])
            for idx, ir in enumerate(intersection_ranges_found):
                if idx == 0:
                    if ir[0] > _range[0]:
                        new_ranges.append((_range[0], ir[0]))

                if idx == len(intersection_ranges_found) - 1:
                    if ir[1] < _range[1]:
                        new_ranges.append((ir[1], _range[1]))
                    continue

                new_ranges.append(
                    (ir[1], intersection_ranges_found[idx + 1][0]))

    final_ranges = new_ranges
    print(final_ranges)

final_ranges.sort(key=lambda x: x[0])
print(final_ranges)
