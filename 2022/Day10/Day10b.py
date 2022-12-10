def printCycle(cycle, X):
    if cycle == 40:
        print()
        cycle = 0
    if cycle == X - 1 or cycle == X or cycle == X + 1:
        print("#", end='')
    else:
        print('.', end='')
    return cycle

with open("Day10_input.txt", "r") as f:
    X = 1
    cycle = 0
    for row in f:
        commands = row.strip().split(" ")
        cycle = printCycle(cycle, X)
        cycle += 1
        if commands[0] == "addx":
            cycle = printCycle(cycle, X)
            cycle += 1
            X += int(commands[1])