from collections import Counter
from enum import Enum


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
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}

JOKER_NUMBER_AND_TYPE_TO_TYPE = {
    1: {
        Types.FOUR: Types.FIVE,
        Types.THREE: Types.FOUR,
        Types.TWO: Types.FULL,
        Types.ONE: Types.THREE,
        Types.HIGH: Types.ONE,
    },  # 1 Joker
    2: {
        Types.FULL: Types.FIVE,
        Types.TWO: Types.FOUR,
        Types.ONE: Types.THREE,
    },  # 2 Jokers
    3: {
        Types.THREE: Types.FOUR,
        Types.FULL: Types.FIVE,
    },  # 3 Jokers
    4: {
        Types.FOUR: Types.FIVE,
    },  # 4 Jokers
    5: {
        Types.FIVE: Types.FIVE,
    },  # 5 Jokers
}


class HandJoker:
    def __init__(self, cards, bid):
        self.cards = cards
        self.cards_values = [CARD_VALUES[x[0]] for x in self.cards]
        self.bid = bid
        self.type = Types.HIGH
        self.__check_hand()

    def __check_hand(self):
        freq = dict(Counter(self.cards))
        if "J" in freq:
            self.type = self.__check_hand_with_Joker(freq)
        else:
            self.type = self.__check_hand_without_Joker(freq)

    def __check_hand_with_Joker(self, freq):
        jokers_number = freq["J"]
        regular_type = self.__check_hand_without_Joker(freq)
        return JOKER_NUMBER_AND_TYPE_TO_TYPE[jokers_number][regular_type]

    def __check_hand_without_Joker(self, freq):
        if self.__isFive(freq):
            return Types.FIVE
        elif self.__isFour(freq):
            return Types.FOUR
        elif self.__isFull(freq):
            return Types.FULL
        elif self.__isThree(freq):
            return Types.THREE
        elif self.__isTwo(freq):
            return Types.TWO
        elif self.__isOne(freq):
            return Types.ONE
        else:
            return Types.HIGH

    def __isFive(self, freq):
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
