limits_of_cubes = {"red": 12, "green": 13, "blue": 14}


def check_if_possible(line, limits_of_cubes):
    id = int(line.split(" ")[1][:-1])
    data = line.split(":")[1]

    for grab in data.split(";"):
        for entry in grab.split(","):
            color = entry.split(" ")[2]
            number = int(entry.split(" ")[1])
            if color in limits_of_cubes.keys():
                if number > limits_of_cubes[color]:
                    return 0
    return id


def calc_power_of_game(line):
    color_values = {"red": 0, "green": 0, "blue": 0}
    data = line.split(":")[1]
    for grab in data.split(";"):
        for entry in grab.split(","):
            color = entry.split(" ")[2]
            number = int(entry.split(" ")[1])
            color_values[color] = max(color_values[color], number)

    return color_values["red"] * color_values["green"] * color_values["blue"]


def resolve_first_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        sum = 0
        for line in data.split("\n"):
            sum += check_if_possible(line, limits_of_cubes)

        return sum


def resolve_second_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        sum = 0
        for line in data.split("\n"):
            sum += calc_power_of_game(line)

        return sum


if __name__ == "__main__":
    print(resolve_first_task("test/data/2/data1.txt"))
    print(resolve_second_task("test/data/2/data2.txt"))
