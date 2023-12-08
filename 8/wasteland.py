with open("input.txt", "r") as f:
    directions = [0 if d == "L" else 1
                  for d in f.readline()[:-1]]
    f.readline()

    nodes = {}
    for line in f.readlines():
        nodes[line.split(" = ")[0]] = (
            line.split("(")[1].split(",")[0],
            line.split(", ")[1].split(")")[0]
        )

    steps = 0
    current_node = "AAA"
    while True:
        for d in directions:
            steps += 1
            current_node = nodes[current_node][d]
            if current_node == "ZZZ":
                break
        else:
            continue
        break

    print(steps)
