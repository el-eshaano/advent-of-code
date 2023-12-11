import readfile

ll = [[int(x) for x in s.split(' ')]
      for s in readfile.line_by_line('test.txt')]


def extrapolate(series):
    diffs = [series]
    while sum(diffs[-1]) != 0:
        diffs.append([e1 - e2 for e1, e2 in zip(diffs[-1][1:], diffs[-1])])

    new_val = 0
    for d in diffs[::-1]:
        new_val = d[0] - new_val

    return new_val


res = 0
for s in ll:
    res += extrapolate(s)

print(res)
