def calculate_score(input):
    hands = input.split(" ")
    match hands[0]:
        case "A": # rock
            match hands[1]:
                case "X": # rock
                    return 4
                case "Y": # paper
                    return 8
                case "Z": # scissors
                    return 3
        case "B": # paper
            match hands[1]:
                case "X": # rock
                    return 1
                case "Y": # paper
                    return 5
                case "Z": # scissors
                    return 9
        case "C": # scissors
            match hands[1]:
                case "X": # rock
                    return 7
                case "Y": # paper
                    return 2
                case "Z": # scissors
                    return 6

with open("Day2_input.txt", "r") as f:
    my_total_score = 0
    for row in f:
        my_total_score += calculate_score(row.strip())
    print(my_total_score)