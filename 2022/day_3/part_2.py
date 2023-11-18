GROUP_SIZE = 3

in_all = []


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
        inventories = []

        for _ in range(GROUP_SIZE):
            inventory = input()
            inventory = [*inventory]
            inventory = set(inventory)
            inventories.append(inventory)
        
        intersection = inventories[0].intersection(*inventories[1:])

        first_item = next(iter(intersection))

        in_all.append(first_item)

except KeyboardInterrupt:
    in_all_priorities = list(map(priority, in_all))
    priorities_sum = sum(in_all_priorities)

    print(in_all)
    print(in_all_priorities)

    print(f"The sum of priorities is {priorities_sum}")
