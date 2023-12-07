from enum import Enum
from collections import Counter


class Types(Enum):
    HIGH = 1
    ONE = 2
    TWO = 3
    THREE = 4
    FULL = 5
    FOUR = 6
    FIVE = 7


CARD_VALUES = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.cards_values = [CARD_VALUES[x[0]] for x in self.cards]
        self.bid = bid
        self.type = Types.HIGH
        self.__check_hand()

    def __check_hand(self):
        freq = dict(Counter(self.cards))
        if self.__isFive():
            self.type = Types.FIVE
        elif self.__isFour(freq):
            self.type = Types.FOUR
        elif self.__isFull(freq):
            self.type = Types.FULL
        elif self.__isThree(freq):
            self.type = Types.THREE
        elif self.__isTwo(freq):
            self.type = Types.TWO
        elif self.__isOne(freq):
            self.type = Types.ONE
        else:
            self.type = Types.HIGH

    def __isFive(self):
        return self.cards.count(self.cards[0]) == len(self.cards)

    def __isFour(self, freq):
        if len(freq) == 2:
            for key in freq:
                if freq[key] == 4:
                    return True
        return False

    def __isFull(self, freq):
        if len(freq) == 2:
            if 3 in freq.values() and 2 in freq.values():
                return True
        return False

    def __isThree(self, freq):
        if len(freq) == 3:
            if 3 in freq.values():
                return True
        return False

    def __isTwo(self, freq):
        if len(freq) == 3:
            if 2 in freq.values():
                return True
        return False

    def __isOne(self, freq):
        if len(freq) == 4:
            return True
        return False

    def __str__(self) -> str:
        return (
            "Hand: "
            + str(self.cards)
            + " Type: "
            + str(self.type)
            + " Bid: "
            + str(self.bid)
            + " Values: "
            + str(self.cards_values)
        )

    def __repr__(self) -> str:
        return (
            "Hand: "
            + str(self.cards)
            + " Type: "
            + str(self.type)
            + " Bid: "
            + str(self.bid)
            + " Values: "
            + str(self.cards_values)
            + "\n"
        )

    def __lt__(self, other):
        if self.type.value < other.type.value:
            return True
        elif self.type.value > other.type.value:
            return False
        else:
            return self.cards_values < other.cards_values

    def getType(self):
        return self.type

    def getBid(self):
        return self.bid
