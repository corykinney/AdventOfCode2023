class AlmanacMap:
    def __init__(self, ranges):
        self.destination_starts, self.source_starts, self.range_lengths = zip(*ranges)

    def __call__(self, num):
        for i in range(len(self.source_starts)):
            if self.source_starts[i] <= num < self.source_starts[i] + self.range_lengths[i]:
                return self.destination_starts[i] + (num - self.source_starts[i])

        return num


with open("input.txt", "r") as f:
    seeds = [int(num) for num in f.readline().split(":")[1].strip().split(" ")]
    f.readline()

    def read_map():
        header = f.readline()  # Skip header
        ranges = []
        while True:  # Read until blank line
            line = f.readline()
            if line.strip() != "":
                ranges.append([int(num) for num in line.split(" ")])
            else:
                return AlmanacMap(ranges)

    seed2soil = read_map()
    soil2fertilizer = read_map()
    fertilizer2water = read_map()
    water2light = read_map()
    light2temperature = read_map()
    temperature2humidity = read_map()
    humidity2location = read_map()

locations = [
    humidity2location(
        temperature2humidity(
            light2temperature(
                water2light(
                    fertilizer2water(
                        soil2fertilizer(
                            seed2soil(
                                seed
                            )
                        )
                    )
                )
            )
        )
    )
    for seed in seeds
]

print(min(locations))
