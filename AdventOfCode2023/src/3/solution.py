SYMBOL_CHARS = ["#", "$", "%", "&", "*", "+", "-", "/", "=", "@"]


class PartNumber:
    def __init__(self, part_number, start_pos, end_pos):
        self.part_number = part_number
        self.start_pos = start_pos
        self.end_pos = end_pos

    def __str__(self):
        return (
            "PartNumber: "
            + self.part_number
            + " StartPos: "
            + str(self.start_pos)
            + " EndPos: "
            + str(self.end_pos)
        )

    def __repr__(self):
        return (
            "PartNumber: "
            + self.part_number
            + " StartPos: "
            + str(self.start_pos)
            + " EndPos: "
            + str(self.end_pos)
        )

    def get_part_number(self):
        return self.part_number

    def get_start_pos(self):
        return self.start_pos

    def get_end_pos(self):
        return self.end_pos


class Symbol:
    def __init__(self, symbol, pos):
        self.symbol = symbol
        self.pos = pos

    def __str__(self):
        return "Symbol: " + self.symbol + " Pos: " + str(self.pos)

    def __repr__(self):
        return "Symbol: " + self.symbol + " Pos: " + str(self.pos)

    def get_symbol(self):
        return self.symbol

    def get_pos(self):
        return self.pos


def load_symbols(data):
    symbols = []
    data = data.split("\n")
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in SYMBOL_CHARS:
                symbols.append(Symbol(data[i][j], (i, j)))
    return symbols


def parse_number(line, start_pos):
    number = ""
    for i in range(start_pos, len(line)):
        if line[i].isdigit():
            number += line[i]
        else:
            return number, i - 1  # -1 because we want to include the last digit
    return number, len(line) - 1  # -1 because we want to include the last digit


def load_numbers(data):
    numbers = []
    data = data.split("\n")
    for i in range(len(data)):
        j = 0
        while j < len(data):
            if data[i][j].isdigit():
                start_pos = j
                new_number, j = parse_number(data[i], j)
                numbers.append(PartNumber(new_number, (i, start_pos), (i, j)))
            j += 1
    return numbers


def are_neighbours(number, symbol):
    if (
        number.get_start_pos()[0] - 1
        <= symbol.get_pos()[0]
        <= number.get_end_pos()[0] + 1
        and number.get_start_pos()[1] - 1
        <= symbol.get_pos()[1]
        <= number.get_end_pos()[1] + 1
    ):
        return True
    return False


def check_neighbours(number, symbols):
    for symbol in symbols:
        if are_neighbours(number, symbol):
            return True
    return False


def check_gear_neighbours(gear, numbers):
    neighbours = []
    for number in numbers:
        if are_neighbours(number, gear):
            neighbours.append(number)
            if len(neighbours) == 2:
                return int(neighbours[0].get_part_number()) * int(
                    neighbours[1].get_part_number()
                )

    return 0


def resolve_first_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()

        symbols = load_symbols(data)
        numbers = load_numbers(data)

        sum = 0

        for number in numbers:
            if check_neighbours(number, symbols):
                sum += int(number.get_part_number())

        return sum


def resolve_second_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()

        symbols = load_symbols(data)
        numbers = load_numbers(data)

        symbols = [x for x in symbols if x.get_symbol() == "*"]

        sum = 0
        for symbol in symbols:
            sum += check_gear_neighbours(symbol, numbers)

        return sum


if __name__ == "__main__":
    print(resolve_first_task("test/data/3/data1.txt"))
    print(resolve_second_task("test/data/3/data2.txt"))
