        for idx, ir in enumerate(intersection_ranges_found):
            if idx == 0:
                if ir[0] > _range[0]:
                    new_ranges.append((_range[0], ir[0]))

            if idx == len(intersection_ranges_found) - 1:
                if ir[1] < _range[1]:
                    new_ranges.append((ir[1], _range[1]))
                continue

            new_ranges.append((ir[1], intersection_ranges_found[idx + 1][0]))