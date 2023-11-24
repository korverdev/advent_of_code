from hashlib import md5


def mine(secret_key: str) -> int:
    """https://adventofcode.com/2015/day/4
    
    >>> mine("abcdef")
    609043
    >>> mine("pqrstuv")
    1048970
    """
    for value in range(0, 10000000):
        key = f"{secret_key}{value}"
        hash = md5(key.encode()).hexdigest()

        if hash.startswith("00000"):
            return value
    
    raise ValueError("No solution found")


if __name__ == "__main__":
    INPUT = "yzbqklnj"

    print("Part 1:")
    print(mine(INPUT))
