# priority of letter = letters.index(letter) + 1
letters = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]

with open("Day3_input.txt", "r") as f:
    sum_of_priorities = 0
    for row in f:
        row1 = row.strip()
        rucksack1 = [x for x in row1]
        row2 = f.readline().strip()
        rucksack2 = [x for x in row2]
        row3 = f.readline().strip()
        rucksack3 = [x for x in row3]
        for item in rucksack1:
            if item in rucksack2 and item in rucksack3:
                sum_of_priorities += letters.index(item) + 1
                break
    print(sum_of_priorities)