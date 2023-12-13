import re

DIRECTIONS = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

NEXT_DIRECTION = {
    "-": {"W": "W", "E": "E"},
    "|": {"N": "N", "S": "S"},
    "L": {"S": "E", "W": "N"},
    "J": {"S": "W", "E": "N"},
    "7": {"N": "W", "E": "S"},
    "F": {"N": "E", "W": "S"},
}


def find_starting_point(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "S":
                return (i, j)


def find_first_step(map, starting_point):
    for dir, move in DIRECTIONS.items():
        current_point = map[starting_point[0] + move[0]][starting_point[1] + move[1]]
        if (
            current_point in NEXT_DIRECTION.keys()
            and dir in NEXT_DIRECTION[current_point].keys()
        ):
            return dir


def find_path(map, starting_point):
    current_point = starting_point

    direction = find_first_step(map, starting_point)
    current_point = (
        current_point[0] + DIRECTIONS[direction][0],
        current_point[1] + DIRECTIONS[direction][1],
    )
    path = [starting_point, current_point]
    while True:
        direction = NEXT_DIRECTION[map[current_point[0]][current_point[1]]][direction]
        current_point = (
            current_point[0] + DIRECTIONS[direction][0],
            current_point[1] + DIRECTIONS[direction][1],
        )
        path.append(current_point)
        if map[current_point[0]][current_point[1]] == "S":
            return path


def calculate_farhtest_point(path):
    return len(path) // 2


def substitute_starting_point(map, starting_point):
    first_dir = ""
    second_dir = ""
    for dir, move in DIRECTIONS.items():
        current_point = map[starting_point[0] + move[0]][starting_point[1] + move[1]]
        if (
            current_point in NEXT_DIRECTION.keys()
            and dir in NEXT_DIRECTION[current_point].keys()
        ):
            if first_dir == "":
                first_dir = dir
            elif second_dir == "":
                second_dir = dir
            else:
                break

    starting_line = list(map[starting_point[0]])

    match first_dir, second_dir:
        case "N", "S":
            starting_line[starting_point[1]] = "|"
        case "W", "E":
            starting_line[starting_point[1]] = "-"
        case "N", "W":
            starting_line[starting_point[1]] = "J"
        case "N", "E":
            starting_line[starting_point[1]] = "L"
        case "S", "W":
            starting_line[starting_point[1]] = "7"
        case "S", "E":
            starting_line[starting_point[1]] = "F"

    map[starting_point[0]] = "".join(starting_line)

    return map


def calculate_tiles_inside_the_path(path, map):
    counter = 0

    map = substitute_starting_point(map, path[0])
    for i in range(len(map)):
        line = list(map[i])
        for j in range(len(map[i])):
            if (i, j) not in path:
                line[j] = "."
        map[i] = "".join(line)

    for line in map:
        line = re.sub(r"L-*7", "|", line)
        line = re.sub(r"L-*J", "||", line)
        line = re.sub(r"F-*7", "||", line)
        line = re.sub(r"F-*J", "|", line)

        is_inside = False
        for c in line:
            if c == "." and is_inside:
                counter += 1
            elif c in "F7LJ|":
                is_inside = not is_inside

    return counter


def resolve_first_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        map = data.split("\n")
        starting_point = find_starting_point(map)
        path = find_path(map, starting_point)
        return calculate_farhtest_point(path)


def resolve_second_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        map = data.split("\n")
        starting_point = find_starting_point(map)
        path = find_path(map, starting_point)

        return calculate_tiles_inside_the_path(path, map)


if __name__ == "__main__":
    print(resolve_first_task("test/data/10/data1.txt"))
    print(resolve_second_task("test/data/10/data2.txt"))
