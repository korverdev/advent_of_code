from dataclasses import dataclass
from enum import Enum, auto
from re import findall, match


class Color(Enum):
    red = auto()
    blue = auto()
    green = auto()


@dataclass
class Game:
    id: int
    red: list[int]
    blue: list[int]
    green: list[int]


MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def _parse(str_: str) -> Game:
    """Parse the string into a Game object.
    
    >>> _parse("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    Game(id=1, red=[4, 1], blue=[3, 6], green=[2, 2])
    """
    tokens = ["[0-9]+"]
    colors = {color.name for color in Color}
    tokens.extend(colors)
    regex = "|".join(tokens)

    id_info, game_info = str_.split(": ")
    id_info = "".join(char for char in id_info if char.isdigit())
    id_info = int(id_info)

    matches = findall(regex, game_info)
    game = Game(id=id_info, red=[], blue=[], green=[])

    value = 0
    for match in matches:
        if match in colors:
            getattr(game, match).append(value)
        else:
            value = int(match)
    
    return game


def play(str_: str) -> int | None:
    """Play a single round of the game.
    
    >>> play("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    1
    >>> play("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    2
    >>> play("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")

    >>> play("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
    
    >>> play("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
    5
    """
    game = _parse(str_)

    for red in game.red:
        if red > MAX_RED:
            return None
    
    for blue in game.blue:
        if blue > MAX_BLUE:
            return None
    
    for green in game.green:
        if green > MAX_GREEN:
            return None

    return game.id


if __name__ == "__main__":
    print("Provide puzzle input:")
    
    strs = []
    try:
        while True:
            strs.append(input())
    
    except KeyboardInterrupt:
        pass

    print("Part 1:")
    result = 0
    for str_ in strs:
        game_id = play(str_)
        if game_id is not None:
            result += game_id
    print(result)
