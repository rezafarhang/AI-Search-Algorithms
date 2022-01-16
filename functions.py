from maze import binary_matrix


def valid(x, y):
    if x < 0 or x > 19 or y < 0 or y > 19:
        return 0
    return 1


def action(x, y):
    possible = []
    if valid(x + 1, y):
        if binary_matrix[x + 1][y] == 1:
            possible.append("down")
    if valid(x - 1, y):
        if binary_matrix[x - 1][y] == 1:
            possible.append("up")
    if valid(x, y + 1):
        if binary_matrix[x][y + 1] == 1:
            possible.append("right")
    if valid(x, y - 1):
        if binary_matrix[x][y - 1] == 1:
            possible.append("left")
    return possible
