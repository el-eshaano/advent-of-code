def line_by_line(filename):
    return [x for x in open(filename).read().strip().split('\n')]

def as_2D_grid(filename):
    return [list(x) for x in open(filename).read().strip().split("\n")]
