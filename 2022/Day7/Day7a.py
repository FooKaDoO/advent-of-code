class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        if parent is not None:
            parent.children.append(self)
        self.children = []
    def printSelf(self, spaces=""):
        print(spaces + "-", self.name, "(dir)")
        for child in self.children:
            child.printSelf(spaces + " ")

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.parent = None
    def add_to_Parent(self, parent):
        self.parent = parent
        parent.size += self.size
        parent.children.append(self)
        while parent.parent is not None:
            parent = parent.parent
            parent.size += self.size
    def printSelf(self, spaces=""):
        print(spaces + "-", self.name, "(file, size="+str(self.size)+")")


with open("Day7_input.txt", "r") as f:
    first_dir = Directory("/", None)
    current_dir = first_dir
    for row in f:
        command = row.strip().split(" ")
        if command[0] == "$":
            if command[1] == "cd":
                if command[2] == "/":
                    current_dir = first_dir
                elif command[2] == "..":
                    current_dir = current_dir.parent
                else:
                    directory_exists = False
                    for item in current_dir.children:
                        if item.name == command[2]:
                            current_dir = item
                            directory_exists = True
                            break
                    if not directory_exists:
                        new_directory = Directory(command[2], current_dir)
            elif command[1] == "ls":
                continue
        elif command[0] == "dir":
            directory_exists = False
            for item in current_dir.children:
                if item.name == command[1]:
                    directory_exists = True
                    break
            if not directory_exists:
                new_directory = Directory(command[1], current_dir)
        else:
            size = int(command[0])
            name = command[1]
            file_exists = False
            for item in current_dir.children:
                if item.name == name:
                    file_exists = True
                    break
            if not file_exists:
                file = File(name, size)
                file.add_to_Parent(current_dir)

def find_sum(directory,max_sum=-1):
    if directory.__class__.__name__ == "File" or directory.__class__.__name__ == "Directory"  and directory.children == []:
        return 0
    sum = 0
    if max_sum == -1 or directory.size <= max_sum:
        sum += directory.size
    for child in directory.children:
        sum += find_sum(child, max_sum)
    return sum

first_dir.printSelf()
sum = find_sum(first_dir, 100000)
print(sum)