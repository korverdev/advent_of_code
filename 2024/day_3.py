import re

def parse(str_: str) -> list[tuple[int, int]]:
    """
    >>> parse("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
    [(2, 4), (5, 5), (11, 8), (8, 5)]
    """
    regex = re.compile(r"mul\(\d+,\d+\)")
    matches = regex.findall(str_)

    values = []
    for match in matches:
        first_value, second_value = map(int, match[4:-1].split(","))
        values.append((first_value, second_value))

    return values

if __name__ == "__main__":
    inputs = []
    try:
        while True:
            if line := input():
                inputs.append(line)
    
    except (KeyboardInterrupt, EOFError):
        pass

    print("User input received. Parsing...")

    parsed_values = [parse(line) for line in inputs]

    print("Parsed values. Calculating...")

    total = 0
    for line in parsed_values:
        for pair in line:
            total += pair[0] * pair[1]
    
    print("(Part 1) Total:", total)
