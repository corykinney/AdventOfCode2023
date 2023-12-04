import numpy as np
import re


pattern = re.compile("[^a-zA-Z0-9_.]")

# Read data
data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(list(line)[:-1])

data = np.asarray(data, dtype="str")
n, m = data.shape

# Get indices of symbols (then set to period)
gears = []
symbols = []
for i in range(n):
    for j in range(m):
        if data[i, j] == "*":
            gears.append((i, j))
        if pattern.match(data[i, j]):
            symbols.append((i, j))
            data[i, j] = "."

# Find numbers
numbers = []
for i in range(n):
    # Keep list of digits and indices in each number
    digits = []
    indices = []
    for j in range(m):
        if data[i, j] != ".":
            digits.append(data[i, j])
            indices.append(j)

        if j == m-1 or data[i, j] == ".":  # Check for end of line or period

            ...

                numbers.append(int("".join(digits)))

            # Reset lists
            digits = []
            indices = []

print(sum(numbers))
