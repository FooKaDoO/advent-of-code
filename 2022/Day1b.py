with open("Day1_input.txt", "r") as f:
    top3 = [0, 0, 0]
    sum = 0
    for row in f:
        row = row.strip()
        if row == "":
            index_of_lowest = top3.index(min(top3))
            if sum > top3[index_of_lowest]:
                top3[index_of_lowest] = sum
            sum = 0
        else:
            sum += int(row)
print(top3[0] + top3[1] + top3[2])