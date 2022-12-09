def distanceXY(H_x, H_y, T_x, T_y):
    add_x = 0
    add_y = 0
    if abs(H_x - T_x) > 1:
        add_x = 1 if H_x - T_x > 1 else -1
        add_y = 1 if H_y > T_y else -1 if H_y < T_y else 0
    elif abs(H_y - T_y) > 1:
        add_y = 1 if H_y - T_y > 1 else -1
        add_x = 1 if H_x > T_x else -1 if H_x < T_x else 0
    return add_x, add_y

def createRope(rope_length):
    rope = []
    while rope_length > 0:
        rope.append([0, 0])
        rope_length -= 1
    return rope

with open("Day9_input.txt", "r") as f:
    rope = createRope(10)
    positions = set()
    positions.add((rope[len(rope)-1][0], rope[len(rope)-1][1]))
    for move in f:
        direction, distance = move.strip().split(" ")
        distance = int(distance)
        amount = 1
        editable = 0
        if direction == "L" or direction == "D":
            amount = -1
        if direction == "D" or direction == "U":
            editable = 1
        while distance > 0:
            i = 0
            rope[i][editable] += amount
            while i < len(rope) - 1:
                add_x, add_y = distanceXY(rope[i][0], rope[i][1], rope[i + 1][0], rope[i + 1][1])
                rope[i + 1][0] += add_x
                rope[i + 1][1] += add_y
                i += 1
            positions.add((rope[i][0], rope[i][1]))
            distance -= 1
    print(len(positions))