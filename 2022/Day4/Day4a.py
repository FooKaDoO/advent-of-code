with open("Day4_input.txt", "r") as f:
    count_of_containing = 0
    for row in f:
        pairs = row.strip().split(",")
        range1 = list(map(int, pairs[0].split("-")))
        range2 = list(map(int, pairs[1].split("-")))
        if range1[0] <= range2[0] and range1[1] >= range2[1] or range2[0] <= range1[0] and range2[1] >= range1[1]:
            count_of_containing += 1
    print(count_of_containing)