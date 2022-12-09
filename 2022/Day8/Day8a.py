with open("Day8_input.txt", "r") as f:
    trees = []
    for row in f:
        row = row.strip()
        tree_row = []
        for tree in row:
            tree_row.append(int(tree))
        trees.append(tree_row)

def isVisible(tree, i, j, trees, coordinate=True, direction=True, first_tree=True):
    if first_tree:
        return isVisible(tree, i + 1, j, trees, True, True, False) or isVisible(tree, i - 1, j, trees, True, False, False) or isVisible(tree, i, j + 1, trees, False, True, False) or isVisible(tree, i, j - 1, trees, False, False, False)
    if i == -1 or j == -1 or i == len(trees) or j == len(trees[i]):
        return True
    if tree <= trees[i][j]:
        return False
    if coordinate:
        if direction:
            return isVisible(tree, i + 1, j, trees, coordinate, direction, first_tree)
        return isVisible(tree, i - 1, j, trees, coordinate, direction, first_tree)
    if direction:
        return isVisible(tree, i, j + 1, trees, coordinate, direction, first_tree)
    return isVisible(tree, i, j - 1, trees, coordinate, direction, first_tree)
'''
def isVisible(tree, i, j, trees, coordinate=True, direction=True, first_tree=True):
    if i == 0 or i == (len(trees) - 1) or j == 0 or (j == len(trees[i]) - 1):
        return True
    if first_tree:
        return isVisible(tree, i, j, trees, True, True, False) or isVisible(tree, i, j, trees, True, False, False) or isVisible(tree, i, j, trees, False, True, False) or isVisible(tree, i, j, trees, False, False, False)
    if coordinate:
        if direction:
            for other_tree in trees[i+1:len(trees)]:
                if other_tree[j] >= tree:
                    return False
            return True
        for other_tree in trees[0:i]:
            if other_tree[j] >= tree:
                return False
        return True
    if direction:
        for other_tree in trees[i][j+1:len(trees[i])]:
            if other_tree >= tree:
                return False
        return True
    for other_tree in trees[i][0:j]:
        if other_tree >= tree:
            return False
    return True
'''


visible_trees = 0
for i, tree_row in enumerate(trees):
    for j, tree in enumerate(tree_row):
        if isVisible(tree, i, j, trees):
            visible_trees += 1
print(visible_trees)