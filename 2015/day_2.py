def surface_area(l: int, w: int, h: int) -> int:
    """https://adventofcode.com/2015/day/2
    
    >>> surface_area(2, 3, 4)
    58
    >>> surface_area(1, 1, 10)
    43
    """
    slack = min(l*w, w*h, h*l)

    return (2*l*w) + (2*w*h) + (2*h*l) + slack


def feet_of_ribbon(l: int, w: int, h: int) -> int:
    """https://adventofcode.com/2015/day/2#part2
    
    >>> feet_of_ribbon(2, 3, 4)
    34
    >>> feet_of_ribbon(1, 1, 10)
    14
    """
    bow = l*w*h
    wrap = (2 * min(l+w, w+h, h+l))
    return bow + wrap


if __name__ == "__main__":

    print("Provide puzzle input:")
    
    dimensions = []

    try:
        while True:
            dimensions.append(input())
            
    except KeyboardInterrupt:
        pass

    total_wrapping_paper = 0
    total_ribbon = 0
    for dimension in dimensions:
        dimension = dimension.split("x")
        dimension = [int(measurement) for measurement in dimension]
        total_wrapping_paper += surface_area(*dimension)
        total_ribbon += feet_of_ribbon(*dimension)

    print("Part 1:")
    print(total_wrapping_paper)

    print("Part 2:")
    print(total_ribbon)
