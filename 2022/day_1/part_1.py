elf_number = 0

calories = [0]

print("Press Ctrl + C to stop inputing values")
print()

try:
    while True:
        calories_input = input()

        if calories_input:
            calories_input = int(calories_input)
            calories[elf_number] += calories_input
        else:
            elf_number += 1
            calories.append(0)

except KeyboardInterrupt:
    max_calories = max(calories)
    elf = calories.index(max_calories) + 1

    print()
    print(f"Elf {elf} is carrying {max_calories} calories.")
