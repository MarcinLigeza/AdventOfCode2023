import numpy as np


class Card:
    def __init__(self, id, winning_numbers=np.array, numbers=np.array):
        self.id = id
        self.winning_numbers = winning_numbers
        self.numbers = numbers

    def __str__(self):
        return (
            "Card: "
            + str(self.id)
            + " WinningNumbers: "
            + str(self.winning_numbers)
            + " Numbers: "
            + str(self.numbers)
        )

    def __repr__(self):
        return (
            "Card: "
            + str(self.id)
            + " WinningNumbers: "
            + str(self.winning_numbers)
            + " Numbers: "
            + str(self.numbers)
        )

    def get_id(self):
        return self.id

    def get_winning_numbers(self):
        return self.winning_numbers

    def get_numbers(self):
        return self.numbers

    def get_matching_numbers_count(self):
        return np.intersect1d(self.winning_numbers, self.numbers).size

    def get_points(self):
        lucky_numbers = np.intersect1d(self.winning_numbers, self.numbers).size
        if lucky_numbers == 0:
            return 0
        return 2 ** (lucky_numbers - 1)


def parse_cards(data):
    cards = []
    data = data.split("\n")
    for line in data:
        numbers = line.split(":")[1].split(" | ")
        winning_numbers = np.fromstring(numbers[0], sep=" ", dtype=int)
        my_numbers = np.fromstring(numbers[1], sep=" ", dtype=int)
        cards.append(Card(line.split(":")[0].split()[1], winning_numbers, my_numbers))
    return cards


def count_cards(cards):
    copies_count = np.ones(len(cards), dtype=int)
    for i in range(len(cards)):
        for j in range(cards[i].get_matching_numbers_count()):
            copies_count[j + i + 1] += copies_count[
                i
            ]  # i + 1 to not increment the current card
    return np.sum(copies_count)


def resolve_first_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()

        cards = parse_cards(data)

        sum = 0

        for card in cards:
            sum += card.get_points()

        return sum


def resolve_second_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()

        cards = parse_cards(data)
        return count_cards(cards)


if __name__ == "__main__":
    print(resolve_first_task("test/data/4/data1.txt"))
    print(resolve_second_task("test/data/4/data2.txt"))
