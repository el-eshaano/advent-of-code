import readfile
import numpy as np

input = readfile.line_by_line('input.txt')

sum = 0
copies = np.ones(len(input))
for cID, c in enumerate(input):
    winning_nums, nums = c.split(":")[1].split("|")
    winning_nums = list(filter(None, winning_nums.split(" ")))
    nums = list(filter(None, nums.split(" ")))

    commons = list(set(winning_nums) & set(nums))
    if len(commons) > 0:
        for i in range(cID + 1, cID + len(commons) + 1):
            copies[i] += copies[cID]

print(copies.astype(int).sum())
