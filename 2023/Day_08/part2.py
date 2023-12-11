import readfile

input = readfile.seperated_by_newlines('input.txt')

instructions = input[0]
nodes_str = input[1].split('\n')

map = {}
nodes = []


for ns in nodes_str:
    key = ns.split("=")[0].strip()
    total_steps_needed = ns.split(", ")[0][-3:]
    r = ns.split(", ")[1][:3]

    if key.endswith('A'):
        nodes.append(key)

    map[key] = [total_steps_needed, r]


def gcd(a, b):

    if b == 0:
        return a

    if a < b:
        return gcd(b, a)

    return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


loop_size = []
for n in nodes:
    steps = 0
    seen = set()
    step = {}
    while True:
        i = 0 if instructions[steps % len(instructions)] == 'L' else 1
        steps += 1

        if (i, n, steps % len(instructions)) in seen:
            loop_size.append(steps - step[n])
            break

        if n.endswith('Z'):
            seen.add((i, n, steps % len(instructions)))
            step[n] = steps

        n = map[n][i]

total_steps_needed = lcm(loop_size[0], loop_size[1])
for i in range(2, len(loop_size)):
    total_steps_needed = lcm(total_steps_needed, loop_size[i])

print(total_steps_needed)
