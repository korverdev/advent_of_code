from re import findall


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


def calibration_value_2(str_: str) -> int:
    """

    # >>> calibration_value_2("two1nine")
    # 29
    # >>> calibration_value_2("eightwothree")
    # 83
    # >>> calibration_value_2("abcone2threexyz")
    # 13
    # >>> calibration_value_2("xtwone3four")
    # 24
    # >>> calibration_value_2("4nineeightseven2")
    # 42
    # >>> calibration_value_2("zoneight234")
    # 14
    # >>> calibration_value_2("7pqrstsixteen")
    # 76
    >>> calibration_value_2("5threeeightwor")
    52
    """
    numbers = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    letters_regex = "|".join(numbers.keys())
    number_regex = "[0-9]"
    regex = f"(?=({letters_regex}|{number_regex}))"
    
    numbers_in_str = findall(regex, str_)
    digits = []
    for number in numbers_in_str:
        if number in numbers.keys():
            digits.append(numbers[number])
        else:
            digits.append(number)

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
    result = sum(calibration_value(str_) for str_ in strs)
    print(result)

    print("Part 2:")
    result = sum(calibration_value_2(str_) for str_ in strs)
    print(result)
