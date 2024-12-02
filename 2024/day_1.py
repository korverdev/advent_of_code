def distance(left: int, right: int) -> int:
    """
    >>> distance(3, 7)
    4
    >>> distance(9, 3)
    6
    """
    return abs(left - right)

def parse(pairs: str) -> tuple[int, int]:
    """
    >>> parse("3   4")
    (3, 4)
    >>> parse("2   5")
    (2, 5)
    >>> parse("1   3")
    (1, 3)
    """
    results = pairs.split()

    assert len(results) == 2

    return (int(results[0]), int(results[1]))


def similarity_score(left: int, right_list: list[int]) -> int:
    """
    >>> similarity_score(3, [4, 3, 5, 3, 9, 3])
    9
    >>> similarity_score(4, [4, 3, 5, 3, 9, 3])
    4
    >>> similarity_score(2, [4, 3, 5, 3, 9, 3])
    0
    """
    instances = len([right for right in right_list if right == left])
    return left * instances


if __name__ == "__main__":
    inputs = []
    try:
        while True:
            if line := input():
                inputs.append(line)
    
    except KeyboardInterrupt:
        pass

    inputs = [parse(line) for line in inputs]

    # Magically split the two lists via arcane BS.
    lists = list(zip(*inputs))
    left_list = sorted(lists[0])
    right_list = sorted(lists[1])
    
    assert len(left_list) == len(right_list)

    distances = [distance(left_val, right_val) for left_val, right_val in zip(left_list, right_list)]
    distances_sum = sum(distances)
    print("(Part 1) Distances:", distances_sum)

    similarities = [similarity_score(left_val, right_list) for left_val in left_list]
    similarities_sum = sum(similarities)
    print("(Part 2) Similarities:", similarities_sum)
