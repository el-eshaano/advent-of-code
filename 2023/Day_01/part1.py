import readfile

if __name__ == "__main__":
    file = 'input.txt'
    input = readfile.line_by_line(file)

    sum = 0
    for s in input:
        digits = [c for c in s if c.isdigit()]
        sum += int(digits[0] + digits[-1])

    print(sum)
