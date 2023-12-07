import re

values = []
with open("input.txt") as f:
    for line in f.readlines():
        digits = re.findall(r"(\d)", line)
        values.append(int("".join([digits[0], digits[-1]])))

print(sum(values))
