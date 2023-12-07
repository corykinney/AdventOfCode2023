import re

values1 = []
values2 = []

num_text = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("input.txt") as f:
    for line in f.readlines():

        # Part one
        digits = re.findall(r"(\d)", line)
        values1.append(int("".join([digits[0], digits[-1]])))

        # Part two
        first_digit = 0
        last_digit = 0

        for i, c in enumerate(line):
            try:  # Check for integer
                int(c)

                if first_digit == 0:  # Set first digit if not set already
                    first_digit = c
                last_digit = c
            except ValueError:
                for j, num in enumerate(num_text):
                    if line[i:i + len(num)] == num:
                        if first_digit == 0:
                            first_digit = str(j + 1)
                        last_digit = str(j + 1)

        values2.append(int("".join([first_digit, last_digit])))

print(sum(values1))
print(sum(values2))
