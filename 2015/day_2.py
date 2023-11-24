def surface_area(l: int, w: int, h: int) -> int:
    """https://adventofcode.com/2015/day/2
    
    >>> surface_area(2, 3, 4)
    58
    >>> surface_area(1, 1, 10)
    43
    """
    slack = min(l*w, w*h, h*l)

    return (2*l*w) + (2*w*h) + (2*h*l) + slack


if __name__ == "__main__":

    print("Provide puzzle input:")
    
    dimensions = []

    try:
        while True:
            dimensions.append(input())
            
    except KeyboardInterrupt:
        pass

    total_square_feet = 0
    for dimension in dimensions:
        dimension = dimension.split("x")
        dimension = [int(measurement) for measurement in dimension]
        total_square_feet += surface_area(*dimension)

    print("Part 1:")
    print(total_square_feet)
