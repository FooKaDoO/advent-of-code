class Monkey:
    def __init__(self, name, starting_items, operation, test, if_true, if_false):
        self.name = name
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = 0
    def throwToMonkey(self, worryLevel):
        if worryLevel % self.test == 0:
            return self.if_true
        return self.if_false
    def worry(self, worryLevel):
        self.inspections += 1
        if self.operation[1] == "+":
            if self.operation[2] == "old":
                return 2*worryLevel
            return worryLevel + int(self.operation[2])
        if self.operation[1] == "*":
            if self.operation[2] == "old":
                return pow(worryLevel, 2)
            return worryLevel*int(self.operation[2])
    def relief(self,worryLevel):
        return worryLevel // 3
    def giveItems(self):
        items = [self.relief(self.worry(worryLevel)) for worryLevel in self.items]
        toMonkey = [self.throwToMonkey(item) for item in items]
        self.items = []
        return list(zip(items, toMonkey))
    def __str__(self):
        return ("Monkey " + self.name + ":\n"
        + "\tItems: " + str(self.items) + "\n"
        + "\tOperation: new = " + str(self.operation) + "\n"
        + "\tTest: divisible by " + str(self.test) + "\n"
        + "\t\tIf true: throw to monkey " + str(if_true) + "\n"
        + "\t\tIf false: throw to monkey " + str(if_false) + "\n")

with open("Day11_input.txt", "r") as f:
    input = f.read().strip().split("\n\n")
monkeys = []
for monkey in input:
    rows = monkey.split("\n")
    name = rows[0].split(" ")[1].split(":")[0]
    starting_items = list(map(int, rows[1].split(": ")[1].split(", ")))
    operation = rows[2].split(" = ")[1].split(" ")
    test = int(rows[3].split("by ")[1])
    if_true = int(rows[4].split("monkey ")[1])
    if_false = int(rows[5].split("monkey ")[1])
    new_monkey = Monkey(name, starting_items, operation, test, if_true, if_false)
    monkeys.append(new_monkey)

for round in range(20):
    for monkey in monkeys:
        items = monkey.giveItems()
        for item, toMonkey in items:
            monkeys[toMonkey].items.append(item)

for monkey in monkeys:
    print("Monkey", monkey.name, "inspected items", monkey.inspections, "times.")
biggest1 = max(monkeys, key=lambda monkey : monkey.inspections)
print(biggest1)
print("Count of inspections:", biggest1.inspections)
monkeys.remove(biggest1)
biggest2 = max(monkeys, key=lambda monkey : monkey.inspections)
print(biggest2)
print("Count of inspections:", biggest2.inspections)
print("Level of monkey business:",biggest1.inspections*biggest2.inspections)