count = 0

try:
    while True:
        line = input()

        if line:
            selection_1, selection_2 = line.split(",")

            start_1, end_1 = selection_1.split("-")
            start_1 = int(start_1)
            end_1 = int(end_1)
            start_2, end_2 = selection_2.split("-")
            start_2 = int(start_2)
            end_2 = int(end_2)

            set_1 = {value for value in range(start_1, end_1 + 1)}
            set_2 = {value for value in range(start_2, end_2 + 1)}

            if set_1.issubset(set_2) or set_2.issubset(set_1):
                count += 1

except KeyboardInterrupt:
    print(f"Overlap: {count}")
