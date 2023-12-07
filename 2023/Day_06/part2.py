import readfile

# super inefficient code, this is a constant time problem
# just need to use some math : range where distance <= x * (time - x)
# but im too lazy lol


input = readfile.line_by_line('input.txt')
time = int(''.join(filter(
    None, input[0].split(":")[1].strip().split(" "))))
distance = int(''.join(filter(
    None, input[1].split(":")[1].strip().split(" "))))

count = 0
for t in range(time+1):
    if t * (time - t) > distance:
        count += 1


print(count)
