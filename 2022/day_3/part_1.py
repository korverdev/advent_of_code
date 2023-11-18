in_both = []


def priority(item: str) -> int:
    character_value = ord(item)

    if item.islower():
        return character_value - ord("a") + 1
    else:
        return character_value - ord("A") + 26 + 1



print("Press Ctrl + C to stop inputing values")
print()

try:
    while True:
        line = input()

        if line:
            # Assuming that line is even.
            midpoint = len(line) // 2

            first_compartment = line[:midpoint]
            second_compartment = line[midpoint:]

            # Split strings into characters.
            first_compartment = [*first_compartment]
            second_compartment = [*second_compartment]

            first_compartment = set(first_compartment)
            second_compartment = set(second_compartment)

            first_item = next(iter(first_compartment.intersection(second_compartment)))

            in_both.append(first_item)

except KeyboardInterrupt:
    in_both_priorities = list(map(priority, in_both))
    priorities_sum = sum(in_both_priorities)

    print(in_both)
    print(in_both_priorities)

    print(f"The sum of priorities is {priorities_sum}")
