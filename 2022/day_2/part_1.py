from enum import Enum


class Choice(Enum):
    rock = 1
    paper = 2
    scissors = 3


class Outcome(Enum):
    lose = 0
    draw = 3
    win = 6


def play(opponents_choice: Choice, your_choice: Choice) -> Outcome:
    if opponents_choice == your_choice:
        return Outcome.draw
    elif (
        (opponents_choice == Choice.rock and your_choice == Choice.paper) or
        (opponents_choice == Choice.paper and your_choice == Choice.scissors) or
        (opponents_choice == Choice.scissors and your_choice == Choice.rock)
    ):
        return Outcome.win
    else:
        return Outcome.lose

print("Press Ctrl + C to stop inputing values")
print()

score = 0

try:
    opponents_choice_key = {
        "A": Choice.rock,
        "B": Choice.paper,
        "C": Choice.scissors,
    }

    your_choice_key = {
        "X": Choice.rock,
        "Y": Choice.paper,
        "Z": Choice.scissors,
    }

    while True:
        line = input()

        # Ignore blank lines.
        if line:
            opponents_choice, your_choice = line.split()
            opponents_choice = opponents_choice_key[opponents_choice]
            your_choice = your_choice_key[your_choice]

            outcome = play(opponents_choice, your_choice)

            score += your_choice.value + outcome.value

except KeyboardInterrupt:
    print(f"Your score is {score}")
