from Hand import Hand
from HandJoker import HandJoker


def resolve_first_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()

        hands = []
        for line in data.split("\n"):
            cards = line.split(" ")[0]
            bid = int(line.split(" ")[1])
            hands.append(Hand(cards, bid))

        result = 0
        hands.sort()
        for i in range(len(hands)):
            result += hands[i].getBid() * (i + 1)

        return result


def resolve_second_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()

        hands = []
        for line in data.split("\n"):
            cards = line.split(" ")[0]
            bid = int(line.split(" ")[1])
            hands.append(HandJoker(cards, bid))

        result = 0
        hands.sort()
        for i in range(len(hands)):
            result += hands[i].getBid() * (i + 1)

        return result


if __name__ == "__main__":
    print(resolve_first_task("test_data/7/data.txt"))
    print(resolve_second_task("test_data/7/data.txt"))
    print(resolve_first_task("private_test_data/7/data.txt"))
    print(resolve_second_task("private_test_data/7/data.txt"))
