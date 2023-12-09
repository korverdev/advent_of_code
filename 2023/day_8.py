from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    value: str
    left: str
    right: str

    def __eq__(self, other: Node) -> bool:
        return self.value == other.value

    def __hash__(self) -> str:
        return self.value


def parse_input(str_: str) -> Node:
    value, directions = str_.split(" = ")
    # Remove () from directions.
    directions = directions[1:-1]
    left, right = directions.split(", ")

    return Node(value, left, right)


def get_node_by_value(nodes: list[Node], value: str) -> Node:
    for node in nodes:
        if node.value == value:
            return node
    
    msg = f"No node found for value {value}"
    raise KeyError(msg)


def steps(inputs: set[str], directions: str) -> set[Node]:
    parsed_inputs = [parse_input(str_) for str_ in inputs]

    upper_bound = 10000
    current_node = parsed_inputs[0]
    for step_count in range(0, upper_bound):
        if current_node.value == "ZZZ":
            return step_count
        
        direction_index = step_count % len(directions)
        direction = directions[direction_index]

        if direction == "L":
            new_node_value = current_node.left
        elif direction == "R":
            new_node_value = current_node.right
        else:
            msg = f"Invalid direction: {direction}"
            raise ValueError(msg)
            
        current_node = get_node_by_value(parsed_inputs, new_node_value)

    msg = f"Upper bound of {upper_bound} steps was hit"
    raise RuntimeError(msg)


if __name__ == "__main__":
    directions = input()

    # Consume empty line.
    input()
    
    inputs = []
    try:
        while True:
            inputs.append(input())
    
    except KeyboardInterrupt:
        pass

    print("Part 1:")
    print(steps(inputs, directions))
