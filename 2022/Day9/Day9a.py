with open("Day9_input.txt", "r") as f:
    H_x = 0
    H_y = 0
    T_x = 0
    T_y = 0
    positions = set()
    positions.add((T_x, T_y))
    for move in f:
        direction, distance = move.strip().split(" ")
        distance = int(distance)
        match direction:
            case "L":
                H_x -= distance
            case "R":
                H_x += distance
            case "D":
                H_y -= distance
            case "U":
                H_y += distance
        while distance > 0:
            add_x = 0
            add_y = 0
            if abs(H_x - T_x) > 1:
                add_x = 1 if H_x - T_x > 1 else -1
                add_y = 1 if H_y > T_y else -1 if H_y < T_y else 0
            elif abs(H_y - T_y) > 1:
                add_y = 1 if H_y - T_y > 1 else -1
                add_x = 1 if H_x > T_x else -1 if H_x < T_x else 0
            T_x += add_x
            T_y += add_y
            positions.add((T_x, T_y))
            distance -= 1
    print(len(positions))