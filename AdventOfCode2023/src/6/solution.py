import numpy as np


def calculate_distance(load_time, race_time):
    return (race_time - load_time) * load_time


# brute force solution
def count_ways_to_win(race_time, current_record):
    counter = 0
    for i in range(1, race_time):
        if calculate_distance(i, race_time) > current_record:
            counter += 1
    return counter


# binary search solution
def find_border_recursive(begin, end, record, race_time):
    if (begin + 1) == end:
        return begin + 1
    middle = (begin + end + 1) // 2
    current_distance = calculate_distance(middle, race_time)
    if current_distance < record:
        return find_border_recursive(middle, end, record, race_time)
    elif current_distance > record:
        return find_border_recursive(begin, middle, record, race_time)
    else:
        return middle + 1


def count_ways_to_win_efficient(race_time, current_record):
    border = find_border_recursive(1, race_time // 2 + 1, current_record, race_time)

    return race_time - 1 - (border - 1) * 2


def resolve_first_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        times = np.fromstring(data.split("\n")[0].split(":")[1], dtype=int, sep=" ")
        distances = np.fromstring(data.split("\n")[1].split(":")[1], dtype=int, sep=" ")

        result = 1
        for i in range(len(times)):
            result *= count_ways_to_win_efficient(times[i], distances[i])

        return result


def resolve_second_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        times = int(data.split("\n")[0].split(":")[1].replace(" ", ""))
        distance = int(data.split("\n")[1].split(":")[1].replace(" ", ""))

        return count_ways_to_win_efficient(times, distance)


if __name__ == "__main__":
    print(resolve_first_task("test/data/6/data1.txt"))
    print(resolve_second_task("test/data/6/data2.txt"))
