with open("Day10_input.txt", "r") as f:
    X = 1
    cycles = 0
    next = 20
    signal_strengths = []
    for row in f:
        command = row.strip().split(" ")
        if command[0] == "noop":
            cycles += 1
            if cycles >= next:
                signal_strengths.append(next*X)
                next += 40
        else:
            cycles += 2
            if cycles >= next:
                signal_strengths.append(next*X)
                next += 40
            X += int(command[1])
    print(sum(signal_strengths))
