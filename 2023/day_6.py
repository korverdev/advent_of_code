def solutions(time: int, distance_record: int) -> int:
    """
    
    >>> solutions(7, 9)
    4
    >>> solutions(15, 40)
    8
    >>> solutions(30, 200)
    9
    """
    result = 0
    for wait_time in range(1, time):
        charge_time = time - wait_time

        attempt = wait_time * charge_time
        if attempt > distance_record:
            result += 1
    
    return result



if __name__ == "__main__":
    print("Provide puzzle input:")
    
    times_input = input()
    distances_input = input()

    times_input = times_input.split(": ")[1]
    distances_input = distances_input.split(": ")[1]

    times = times_input.split()
    distances = distances_input.split()

    times = [int(x) for x in times]
    distances = [int(x) for x in distances]

    print("Part 1:")
    margin_for_error = 0
    for time, distance in zip(times, distances):
        x = solutions(time, distance)

        if not margin_for_error:
            margin_for_error = x
        else:
            margin_for_error *= x
    print(margin_for_error)


    print("Part 2:")
    time = "".join(times_input.split())
    distance = "".join(distances_input.split())
    time = int(time)
    distance = int(distance)

    print(solutions(time, distance))
