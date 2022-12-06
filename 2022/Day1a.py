with open("Day1_input.txt", "r") as f:
    max = 0
    sum = 0
    for row in f:
        row = row.strip()
        if row == "":
            if sum > max:
                max = sum
            sum = 0
        else:
            sum += int(row)
print(max)