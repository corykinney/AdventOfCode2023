import re
import numpy as np

pattern = r"\s(\d+)(?=\s)"
with open("input.txt", "r") as f:
    times = [int(num) for num in re.findall(pattern, f.readline())]
    distances = [int(num) for num in re.findall(pattern, f.readline())]

ways = []
for t, d in zip(times, distances):
    x = np.arange(t + 1)
    y = x * (t - x)
    ways.append(np.count_nonzero(y > d))

print(np.prod(ways))
