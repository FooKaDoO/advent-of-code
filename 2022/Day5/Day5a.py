'''
        [J]         [B]     [T]
        [M] [L]     [Q] [L] [R]
        [G] [Q]     [W] [S] [B] [L]
[D]     [D] [T]     [M] [G] [V] [P]
[T]     [N] [N] [N] [D] [J] [G] [N]
[W] [H] [H] [S] [C] [N] [R] [W] [D]
[N] [P] [P] [W] [H] [H] [B] [N] [G]
[L] [C] [W] [C] [P] [T] [M] [Z] [W]
 1   2   3   4   5   6   7   8   9
'''

with open("Day5_input.txt", "r") as f:
    stacks_input, stacks_operations = f.read().split("\n\n")
stacks = []
stacks_lines = stacks_input.split("\n")
count_of_stacks = round((len(stacks_lines.pop()) + 1) / 4)
for i in range(count_of_stacks):
    stacks.append([])
for row in stacks_lines:
    for i in range(count_of_stacks):
        element = row[4*i+1:4*i+2]
        if element != " " and element != "":
            stacks[i].append(element)

for i in range(count_of_stacks):
    stacks[i].reverse()

stacks_operations_lines = stacks_operations.split("\n")
for row in stacks_operations_lines:
    words = row.split(" ")
    how_many = int(words[1])
    stack_from = int(words[3])-1
    stack_to = int(words[5])-1
    for i in range(how_many):
        stacks[stack_to].append(stacks[stack_from].pop())

return_value = ""
for stack in stacks:
    return_value += stack.pop()
print(return_value)
