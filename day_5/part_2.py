MAX_CRATE_STACKS = 9


def clean_crate_input(str_: str) -> str:
    return str_.strip("[] ")


crate_stacks = [[] for _ in range(MAX_CRATE_STACKS)]


try:
    # Fill initial crate stacks.
    while True:
        line = input()

        if line.strip():
            # If line lists crates.
            if line.strip()[0] == "[":
                space_between_crates = 4
                crates = [clean_crate_input(line[index:index+space_between_crates]) for index in range(0, len(line), space_between_crates)]

                for index, crate in enumerate(crates):
                    if crate:
                        crate_stacks[index].insert(0, crate)

        else:
            break
    
    while True:
        words = input().split()

        amount_of_crates = int(words[1])
        from_stack = int(words[3]) - 1
        to_stack = int(words[5]) - 1

        temp_crates = []
        for _ in range(amount_of_crates):
            crate = crate_stacks[from_stack].pop()
            temp_crates.insert(0, crate)

        crate_stacks[to_stack].extend(temp_crates)

except KeyboardInterrupt:
    message = []

    for stack in crate_stacks:
        if stack:
            message.append(stack.pop())
    
    print("".join(message))
