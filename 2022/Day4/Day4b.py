with open("Day4_input.txt", "r") as f:
    count_of_containing = 0
    for row in f:
        pairs = row.strip().split(",")
        range1 = list(map(int, pairs[0].split("-")))
        range2 = list(map(int, pairs[1].split("-")))
        first_elf_work = range(range1[0], range1[1] + 1)
        second_elf_work = range(range2[0], range2[1] + 1)
        if range1[0] in second_elf_work or range1[1] in second_elf_work or range2[0] in first_elf_work or range2[1] in first_elf_work:
            count_of_containing += 1
    print(count_of_containing)