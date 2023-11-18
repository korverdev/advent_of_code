TOP_X = 3

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
    top_x_calories = 0

    for inc in range(TOP_X):
        max_calories = max(calories)
        index = calories.index(max_calories)
        calories[index] = 0

        top_x_calories += max_calories

        print()
        print(f"{inc+1}. Elf {index + 1} is carrying {max_calories} calories.")

    print(f"The top {TOP_X} elves are carrying {top_x_calories} calories in total")
