# priority of letter = letters.index(letter) + 1
letters = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]

with open("Day3_input.txt", "r") as f:
    sum_of_priorities = 0
    for row in f:
        rucksack = [x for x in row.strip()]
        mid_point = int(len(rucksack)/2)
        first_compartment = rucksack[:mid_point]
        second_compartment = rucksack[mid_point:]
        for item in first_compartment:
            if item in second_compartment:
                sum_of_priorities += letters.index(item) + 1
                break
    print(sum_of_priorities)