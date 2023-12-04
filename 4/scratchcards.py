import re

pattern = r"\s(\d+)(?=\s)"

scores = []
with open("input.txt") as f:
    for line in f.readlines():
        winning, present = line.split(":")[1].split("|")
        winning = set([int(num) for num in re.findall(pattern, winning)])
        present = set([int(num) for num in re.findall(pattern, present)])
        if (matched := len(winning.intersection(present))) != 0:
            scores.append(2**(matched - 1))

print(sum(scores))
