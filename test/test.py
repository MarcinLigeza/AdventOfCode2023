import importlib
import os
import sys

SRC_DIR = "AdventOfCode2023/src/"

TEST_DATA_DIR = "test/data/"

DATA1_FILE = "/data1.txt"
DATA2_FILE = "/data2.txt"

RESULT1_FILE = "/result1.txt"
RESULT2_FILE = "/result2.txt"


def get_ready_solutions():
    return sorted(os.listdir(SRC_DIR))


def test_solution(day_number):
    sys.path.append(os.path.abspath(SRC_DIR))
    sys.path.append(os.path.abspath(SRC_DIR + day_number))

    solution = importlib.import_module(day_number + ".solution")
    print("Testing " + day_number + "...")
    with open(TEST_DATA_DIR + day_number + RESULT1_FILE, "r") as f:
        expected_result1 = int(f.read())
        result1 = solution.resolve_first_task(TEST_DATA_DIR + day_number + DATA1_FILE)
        assert result1 == expected_result1, (
            "Expected: " + str(expected_result1) + ", got: " + str(result1)
        )

    with open(TEST_DATA_DIR + day_number + RESULT2_FILE, "r") as f:
        expected_result2 = int(f.read())
        result2 = solution.resolve_second_task(TEST_DATA_DIR + day_number + DATA2_FILE)
        assert result2 == expected_result2, (
            "Expected: " + str(expected_result2) + ", got: " + str(result2)
        )

    print("Tests passed for " + day_number)


if __name__ == "__main__":
    for i in get_ready_solutions():
        test_solution(i)
    print("All tests passed!")
