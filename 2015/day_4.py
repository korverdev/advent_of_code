from hashlib import md5


def mine(secret_key: str, zeros: int = 5) -> int:
    """https://adventofcode.com/2015/day/4
    
    >>> mine("abcdef")
    609043
    >>> mine("pqrstuv")
    1048970
    """
    for value in range(0, 10000000):
        key = f"{secret_key}{value}"
        hash = md5(key.encode()).hexdigest()

        if hash.startswith("0" * zeros):
            return value
    
    raise ValueError("No solution found")


if __name__ == "__main__":
    INPUT = "yzbqklnj"

    print("Part 1:")
    print(mine(INPUT))

    print("Part 2:")
    print(mine(INPUT, 6))
