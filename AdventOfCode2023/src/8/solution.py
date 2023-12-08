from math import lcm

STARTING_NODE = "AAA"
END_NODE = "ZZZ"


def parse_nodes(data):
    nodes = {}
    for line in data.split("\n"):
        line = line.replace("(", "").replace(")", "").split(" = ")
        node_name = line[0].replace(" ", "")
        node_L = line[1].split(",")[0].replace(" ", "")
        node_R = line[1].split(",")[1].replace(" ", "")
        nodes[node_name] = {"L": node_L, "R": node_R}

    return nodes


def find_path(nodes, sequence):
    counter = 0

    current_node = STARTING_NODE

    while True:
        for dir in sequence:
            counter += 1
            if nodes[current_node][dir] == END_NODE:
                return counter
            else:
                current_node = nodes[current_node][dir]


def check_all_nodes_finished(current_nodes):
    for node in current_nodes:
        if not node[-1] == "Z":
            return False
    return True


def find_path_multiple_nodes(nodes, sequence, starting_nodes):
    counter = 0
    circle_lengths = {}
    nodes_to_check = starting_nodes.copy()

    while len(nodes_to_check) > 0:
        for dir in sequence:
            counter += 1
            nodes_to_be_removed = []
            for i in range(len(nodes_to_check)):
                nodes_to_check[i] = nodes[nodes_to_check[i]][dir]
                if nodes_to_check[i][-1] == "Z":
                    circle_lengths[nodes_to_check[i]] = counter
                    nodes_to_be_removed.append(nodes_to_check[i])

            for node in nodes_to_be_removed:
                nodes_to_check.remove(node)

    return lcm(*circle_lengths.values())


def resolve_first_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()

        sequence = data.split("\n\n")[0]
        nodes = parse_nodes(data.split("\n\n")[1])

        return find_path(nodes, sequence)


def resolve_second_task(file_name):
    with open(file_name, "r") as f:
        data = f.read()

        sequence = data.split("\n\n")[0]
        nodes = parse_nodes(data.split("\n\n")[1])

        starting_nodes = [x for x in nodes.keys() if x[-1] == "A"]

        return find_path_multiple_nodes(nodes, sequence, starting_nodes)


if __name__ == "__main__":
    print(resolve_first_task("test/data/8/data1.txt"))
    print(resolve_second_task("test/data/8/data2.txt"))
