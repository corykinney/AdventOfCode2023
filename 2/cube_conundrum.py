import re

red, green, blue = 12, 13, 14

games = []
powers = []
with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        r = max([int(num) for num in re.findall(r"(\d+) red", line)])
        g = max([int(num) for num in re.findall(r"(\d+) green", line)])
        b = max([int(num) for num in re.findall(r"(\d+) blue", line)])

        if r <= red and g <= green and b <= blue:
            games.append(i + 1)

        powers.append(r * g * b)

print(sum(games))
print(sum(powers))
