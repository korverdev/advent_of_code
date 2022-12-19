cycle = 0
register = 1
signals = []

def run_cycle(cycle, cycles):
    for _ in range(cycles):
        cycle += 1

        if not ((cycle - 20) % 40):
            signal_strength = cycle * register
            print(f"Cycle: {cycle} - Register: {register} - Signal Strength: {signal_strength}")

            signals.append(signal_strength)
    
    return cycle

try:
    while True:
        command = input()
        command = command.split()

        if command[0] == "addx":
            cycle = run_cycle(cycle, 2)
            register += int(command[1])
        elif command[0] == "noop":
            cycle = run_cycle(cycle, 1)

except KeyboardInterrupt:
    print("Sum of signal strengths:", sum(signals))