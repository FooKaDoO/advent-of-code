with open("Day6_input.txt", "r") as f:
    buffer = f.read()
packet = []
for i, char in enumerate(buffer):
    if len(packet) == 14:
        packet = packet[1:]
    packet += [char]
    if len(set(packet)) == 14:
        print(i + 1)
        break