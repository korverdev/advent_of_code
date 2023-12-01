def calibration_value(str_: str) -> int:
    """
    
    >>> calibration_value("1abc2")
    12
    >>> calibration_value("pqr3stu8vwx")
    38
    >>> calibration_value("a1b2c3d4e5f")
    15
    >>> calibration_value("treb7uchet")
    77
    """
    digits = [char for char in str_ if char.isdigit()]
    first_digit = digits[0]
    last_digit = digits[-1]

    two_digit_number = f"{first_digit}{last_digit}"
    return int(two_digit_number)


if __name__ == "__main__":
    print("Provide puzzle input:")

    strs = []

    try:
        while True:
            strs.append(input())
            
    except KeyboardInterrupt:
        pass

    print("Part 1:")
    sum = sum(calibration_value(str_) for str_ in strs)
    print(sum)
