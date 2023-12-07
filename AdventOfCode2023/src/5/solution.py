import sys

import numpy as np


def parse_seeds(line):
    line = line.split(":")[1]
    seeds = np.fromstring(line, dtype=int, sep=" ")
    return seeds


class Map:
    def __init__(self, name, mapping):
        self.name = name
        self.mapping = mapping

    def __str__(self):
        return "Map: " + self.name + " Mapping: " + str(self.mapping)

    def __repr__(self):
        return "Map: " + self.name + " Mapping: " + str(self.mapping)

    def get_name(self):
        return self.name

    def get_mapping(self):
        return self.mapping

    def get_value(self, x):
        for line in self.mapping:
            if line[1] <= x < line[1] + line[2]:
                return line[0] + x - line[1]
        return x

    def get_value_reversed(self, x):
        for line in self.mapping:
            if line[0] <= x < line[0] + line[2]:
                return line[1] + x - line[0]
        return x


def parse_map(data):
    data = data.split(":")
    name = data[0]
    mapping = []
    for line in data[1].split("\n")[1:]:
        mapping.append(np.fromstring(line, dtype=int, sep=" "))

    return Map(name, mapping)


def parse_input(data):
    sections = data.split("\n\n")
    seeds = parse_seeds(sections[0])
    maps = []
    for section in sections[1:]:
        maps.append(parse_map(section))
    return seeds, maps


def find_seed_location(seed, maps):
    result = seed
    for map in maps:
        result = map.get_value(result)
    return result


def find_location_seed(location, maps):
    result = location
    for map in reversed(maps):
        result = map.get_value_reversed(result)
    return result


def check_if_seed_exists(seeds, s):
    for seed in seeds:
        if seed[0] <= s < seed[0] + seed[1]:
            return True


def resolve_first_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        seeds, maps = parse_input(data)

        lowest_location = sys.maxsize * 2 + 1
        for seed in seeds:
            location = find_seed_location(seed, maps)
            lowest_location = min(lowest_location, location)

        return lowest_location


def resolve_second_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        seeds, maps = parse_input(data)

        seeds_ranges = list(zip(seeds[::2], seeds[1::2]))

        for i in range(sys.maxsize * 2 + 1):
            seed = find_location_seed(i, maps)
            if check_if_seed_exists(seeds_ranges, seed):
                return i

        # BRUTE FORCE SOLUTION

        # lowest_location = sys.maxsize * 2 + 1

        # for seed_range in seeds_ranges:
        #     for i in range(seed_range[0], seed_range[0] + seed_range[1]):
        #         location = find_seed_location(i, maps)
        #         lowest_location = min(lowest_location, location)

        # return lowest_location


if __name__ == "__main__":
    print(resolve_first_task("test/data/5/data1.txt"))
    print(resolve_second_task("test/data/5/data2.txt"))
