import numpy as np


def get_coordinates_of_stars(map):
    stars = []
    for row_number, row in enumerate(map):
        for column_number, cell in enumerate(row):
            if cell == "#":
                stars.append((row_number, column_number))
    return stars


def calculate_distance_between_stars(star1, star2, map):
    distance = 0
    for i in range(star2[0] - star1[0]):
        distance += map[star1[0] + i, star1[1]]
    for i in range(abs(star2[1] - star1[1])):
        if star1[1] < star2[1]:
            distance += map[star2[0], star1[1] + i]
        else:
            distance += map[star2[0], star1[1] - i]
    return distance


def get_shortest_path_expanded(stars, map):
    distance = 0
    for i, star in enumerate(stars):
        for other_star in stars[i + 1 :]:
            distance += calculate_distance_between_stars(star, other_star, map)

    return distance


def parse_map(map):
    new_map = np.zeros((len(map), len(map[0])), dtype=int)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "#":
                new_map[i, j] = 0
            else:
                new_map[i, j] = 1
    return new_map


def expand_map(map, factor=1):
    new_map = np.ones((len(map), len(map[0])), dtype=int)
    rows_to_double = []
    columns_to_double = []

    for index, row in enumerate(map):
        if all([cell == "." for cell in row]):
            rows_to_double.append(index)
    for index, column in enumerate(zip(*map)):
        if all([cell == "." for cell in column]):
            columns_to_double.append(index)

    for index in rows_to_double[::-1]:
        new_map[index, :] = new_map[index, :] * factor
    for index in columns_to_double[::-1]:
        new_map[:, index] = new_map[:, index] * factor

    return new_map


def resolve_first_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        map = data.split("\n")
        stars = get_coordinates_of_stars(map)
        distances_map = expand_map(map, 2)
        return get_shortest_path_expanded(stars, distances_map)


def resolve_second_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        map = data.split("\n")
        stars = get_coordinates_of_stars(map)
        distances_map = expand_map(map, 1000000)
        return get_shortest_path_expanded(stars, distances_map)


if __name__ == "__main__":
    print(resolve_first_task("test/data/11/data1.txt"))
    print(resolve_second_task("test/data/11/data2.txt"))
