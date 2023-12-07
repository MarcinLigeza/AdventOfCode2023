"""
Solution to the first day of the advent of code 2023.
"""
import sys

digits_to_values = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_first_and_last_digit(line):
    """
    Get the first and last digit in a line.
    """
    first = 0
    last = 0
    for i in line:
        if i.isdigit():
            first = int(i)
            break
    for i in reversed(line):
        if i.isdigit():
            last = int(i)
            break
    return first, last


def find_first_occurence(line, digits_to_values):
    pos = sys.maxsize * 2 + 1
    value = 0
    for digit in digits_to_values.keys():
        new_position = line.find(digit)
        if new_position != -1 and new_position < pos:
            pos = new_position
            value = digits_to_values[digit]

    return value


def find_last_occurence(line, digits_to_values):
    pos = -1
    value = 0
    for digit in digits_to_values.keys():
        new_position = line.rfind(digit)
        if new_position != -1 and new_position > pos:
            pos = new_position
            value = digits_to_values[digit]

    return value


def get_first_and_last_digit_2(line):
    """
    Get the first and last digit (including english spelled words) in a line.
    """
    first = find_first_occurence(line, digits_to_values)
    last = find_last_occurence(line, digits_to_values)
    return first, last


def resolve_first_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        sum = 0
        for line in data.split("\n"):
            first, last = get_first_and_last_digit(line)
            sum += first * 10 + last

        return sum


def resolve_second_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        sum = 0
        for line in data.split("\n"):
            first, last = get_first_and_last_digit_2(line)
            sum += first * 10 + last

        return sum


if __name__ == "__main__":
    print(resolve_first_task("test_data/1/data1.txt"))
    print(resolve_second_task("test_data/1/data2.txt"))
