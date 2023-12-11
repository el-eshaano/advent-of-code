import readfile

input = readfile.seperated_by_newlines('input.txt')

instructions = input[0]
nodes = input[1].split('\n')

map = {}
for ns in nodes:
    key = ns.split("=")[0].strip()
    l = ns.split(", ")[0][-3:]
    r = ns.split(", ")[1][:3]

    map[key] = [l, r]

steps = 0
curr_node = 'AAA'
while curr_node != 'ZZZ':
    i = 0 if instructions[steps % len(instructions)] == 'L' else 1
    curr_node = map[curr_node][i]

    steps += 1

print(steps)
