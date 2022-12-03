from enum import Enum


class Choice(Enum):
    rock = 1
    paper = 2
    scissors = 3


class Outcome(Enum):
    lose = 0
    draw = 3
    win = 6


def your_choice(opponents_choice: Choice, desired_outcome: Outcome) -> Choice:
    if desired_outcome == Outcome.draw:
        return opponents_choice

    elif desired_outcome == Outcome.win:
        if opponents_choice == Choice.rock:
            return Choice.paper
        elif opponents_choice == Choice.paper:
            return Choice.scissors
        else:
            return Choice.rock

    else:
        if opponents_choice == Choice.rock:
            return Choice.scissors
        elif opponents_choice == Choice.paper:
            return Choice.rock
        else:
            return Choice.paper


print("Press Ctrl + C to stop inputing values")
print()

score = 0

try:
    opponents_choice_key = {
        "A": Choice.rock,
        "B": Choice.paper,
        "C": Choice.scissors,
    }

    desired_outcome_key = {
        "X": Outcome.lose,
        "Y": Outcome.draw,
        "Z": Outcome.win,
    }

    while True:
        line = input()

        # Ignore blank lines.
        if line:
            opponents_choice, desired_outcome = line.split()
            opponents_choice = opponents_choice_key[opponents_choice]
            desired_outcome = desired_outcome_key[desired_outcome]

            choice = your_choice(opponents_choice, desired_outcome)

            score += desired_outcome.value + choice.value

except KeyboardInterrupt:
    print(f"Your score is {score}")
