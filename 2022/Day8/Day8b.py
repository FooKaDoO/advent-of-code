with open("Day8_input.txt", "r") as f:
    trees = []
    for row in f:
        row = row.strip()
        tree_row = []
        for tree in row:
            tree_row.append(int(tree))
        trees.append(tree_row)

def scenicVal(tree, i, j, trees):
    up = 0
    down = 0
    left = 0
    right = 0

    coordinate_x = i - 1
    while coordinate_x >= 0:
        if trees[coordinate_x][j] >= tree:
            up += 1
            break
        up += 1
        coordinate_x -= 1
    coordinate_x = i + 1
    while coordinate_x < len(trees):
        if trees[coordinate_x][j] >= tree:
            down += 1
            break
        down += 1
        coordinate_x += 1

    coordinate_y = j - 1
    while coordinate_y >= 0:
        if trees[i][coordinate_y] >= tree:
            left += 1
            break
        left += 1
        coordinate_y -= 1
    coordinate_y = j + 1
    while coordinate_y < len(trees[i]):
        if trees[i][coordinate_y] >= tree:
            right += 1
            break
        right += 1
        coordinate_y += 1
    return up*down*left*right

best_val = 0
for i, tree_row in enumerate(trees):
    for j, tree in enumerate(tree_row):
        current_val = scenicVal(tree, i, j, trees)
        if current_val > best_val:
            best_val = current_val
print(best_val)