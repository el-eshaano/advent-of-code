import readfile

input = readfile.line_by_line('input.txt')

sum = 0
for cID, c in enumerate(input):
    winning_nums, nums = c.split(":")[1].split("|")
    winning_nums = list(filter(None, winning_nums.split(" ")))
    nums = list(filter(None, nums.split(" ")))

    commons = list(set(winning_nums) & set(nums))
    if len(commons) > 0:
        sum += 2 ** (len(commons) - 1)

print(sum)
