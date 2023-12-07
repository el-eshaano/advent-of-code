import readfile

# distance travelled = speed * remaining_time
# d = charge_up_time * remaining_time

input = readfile.line_by_line('input.txt')
times = [int(x) for x in filter(
    None, input[0].split(":")[1].strip().split(" "))]
distances = [int(x) for x in filter(
    None, input[1].split(":")[1].strip().split(" "))]

prod = 1
for i in range(len(times)):
    count = 0
    time, distance = times[i], distances[i]
    for t in range(time+1):
        if t * (time - t) > distance:
            count += 1

    prod *= count

print(prod)
