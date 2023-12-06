import re
import numpy as np

pattern = r"\s(\d+)(?=\s)"
with open("input.txt", "r") as f:
    times = re.findall(pattern, f.readline())
    distances = re.findall(pattern, f.readline())

# Part 1
ways = []
for t, d in zip(times, distances):
    x = np.arange(int(t) + 1)
    y = x * (int(t) - x)
    ways.append(np.count_nonzero(y > int(d)))

print(np.prod(ways))

# Part 2
t = int("".join(times))
d = int("".join(distances))

x1 = np.ceil((t - (t**2 - 4*d)**0.5) / 2)
x2 = np.floor((t + (t**2 - 4*d)**0.5) / 2)
print(int(x2 - x1 + 1))
