from dataclasses import dataclass, field
from typing import Iterator


@dataclass
class Number:
    value: int
    coordinates: set[tuple] = field(default_factory=set)


def parse_numbers(str_: str, y: int) -> Iterator[Number]:
    number = ""
    coordinates = set()
    for x, char in enumerate(str_):
        if char.isdigit():
            number += char
            coordinates.add((x, y))

        elif number:
            yield Number(int(number), coordinates)
            number = ""
            coordinates = set()

def parse_symbols(str_: str, y: int) -> set[tuple[int]]:
    result = set()
    for x, char in enumerate(str_):
        if not char.isdigit() and not char == ".":
            result.add((x, y))
    
    return result


def check_coordinate(coordinate: tuple[int], symbols: set[tuple[int]]) -> bool:
    """
    
    >>> check_coordinate((1, 1), {(2, 2)})
    True
    """
    for x in range(coordinate[0] - 1, coordinate[0] + 2):
        for y in range(coordinate[1] - 1, coordinate[1] + 2):
            if (x, y) in symbols:
                return True
    
    return False


def check_around(number: Number, symbols: set[tuple[int]]) -> bool:
    for coordinate in number.coordinates:
        if check_coordinate(coordinate, symbols):
            return True
        
    return False


if __name__ == "__main__":
    print("Provide puzzle input:")
    
    strs = []
    try:
        while True:
            strs.append(input())
    
    except KeyboardInterrupt:
        pass

    print("Part 1:")
    numbers: list[Number] = []
    symbols = set()
    for y, str_ in enumerate(strs):
        numbers.extend(parse_numbers(str_, y))

        symbols.update(parse_symbols(str_, y))

    result = 0
    for number in numbers:
        if check_around(number, symbols):
            result += number.value
    print(result)
