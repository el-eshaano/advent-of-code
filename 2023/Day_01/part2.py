import readfile

if __name__ == "__main__":
    filename = 'input.txt'
    input = readfile.line_by_line(filename)

    sum = 0
    for s in input:
        s = s.replace("one", "o1e").replace("two", "t2o").replace("three", "th3ee").replace("four", "f4ur").replace("five", "f5ve").replace("six", "s6x").replace("seven", "se7en").replace("eight", "ei8ht").replace("nine", "n9ne").replace("zero", "z0ro")
        
        digits = [c for c in s if c.isdigit()]
        sum += int(digits[0] + digits[-1])

    print(sum)
