import numpy as np


def calculte_extrapolation(sequence):
    result = 0

    sequence = np.array([int(s) for s in sequence.split(" ")])
    last_column = np.array([sequence[-1]])

    current_sequence = sequence

    while any(x != 0 for x in current_sequence):
        for i in range(len(current_sequence) - 1):
            current_sequence[i] = current_sequence[i + 1] - current_sequence[i]
        current_sequence = current_sequence[:-1]
        last_column = np.append(last_column, current_sequence[-1])
    result = sum(last_column)

    return result


def calculate_backward_extrapolation(sequence):
    result = 0

    sequence = np.array([int(s) for s in sequence.split(" ")])
    first_column = np.array([sequence[0]])

    current_sequence = sequence

    while any(x != 0 for x in current_sequence):
        for i in range(len(current_sequence) - 1):
            current_sequence[i] = current_sequence[i + 1] - current_sequence[i]
        current_sequence = current_sequence[:-1]
        first_column = np.append(first_column, current_sequence[0])

    for number in first_column[::-1]:
        result = number - result

    return result


def resolve_first_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()

        sequences = data.split("\n")
        sum = 0
        for sequence in sequences:
            sum += calculte_extrapolation(sequence)
        return sum


def resolve_second_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()

        sequences = data.split("\n")
        sum = 0
        for sequence in sequences:
            sum += calculate_backward_extrapolation(sequence)
        return sum


if __name__ == "__main__":
    print(resolve_first_task("test/data/9/data1.txt"))
    print(resolve_second_task("test/data/9/data2.txt"))
