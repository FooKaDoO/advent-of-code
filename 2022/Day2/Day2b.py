def calculate_score(input):
    hands = input.split(" ")
    match hands[0]:
        case "A": # rock
            match hands[1]:
                case "X": # lose
                    return 3 # scissors
                case "Y": # draw
                    return 4 # rock
                case "Z": # win
                    return 8 # paper
        case "B": # paper
            match hands[1]:
                case "X": # lose
                    return 1 # rock
                case "Y": # draw
                    return 5 # paper
                case "Z": # win
                    return 9 # scissors
        case "C": # scissors
            match hands[1]:
                case "X": # lose
                    return 2 # paper
                case "Y": # draw
                    return 6  # scissors
                case "Z": # win
                    return 7 # rock

with open("Day2_input.txt", "r") as f:
    my_total_score = 0
    for row in f:
        my_total_score += calculate_score(row.strip())
    print(my_total_score)