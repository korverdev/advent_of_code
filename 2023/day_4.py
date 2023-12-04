def points(winners: list[int], yours: list[int]) -> int:
    count = 0
    for number in yours:
        if number in winners:
            count += 1

    return pow(2, count - 1) if count else 0


def parse(str_: str) -> int:
    """
    
    >>> parse("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    8
    >>> parse("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19")
    2
    >>> parse("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1")
    2
    >>> parse("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83")
    1
    >>> parse("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36")
    0
    >>> parse("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")
    0
    """
    # Trim off the "Card 1: " part
    str_ = str_.split(": ")[1]

    winners, yours = str_.split(" | ")
    winners = winners.split()
    yours = yours.split()

    return points(winners, yours)


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
        result += parse(str_)
    print(result)
