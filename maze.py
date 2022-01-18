maze = [
    ['-', '-', 'H', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'W', 'W', '-', '-', '-', 'W', '-', '-'],
    ['-', '-', 'W', '-', 'W', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['H', 'H', '-', '-', '-', 'W', '-', '-', '-', '-', '-', 'W', '-', '-', '-', 'H', '-', 'W', '-', '-'],
    ['-', '-', '-', '-', '-', '-', 'F', '-', '-', '-', '-', '-', '-', '-', 'W', '-', '-', '-', '-', '-'],
    ['-', '-', '-', 'W', '-', 'W', '-', '-', '-', 'W', '-', '-', '-', '-', 'W', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', 'H', '-', '-', '-', '-', '-', '-', 'W', '-', '-', '-'],
    ['W', '-', '-', '-', '-', 'H', '-', '-', '-', '-', '-', '-', '-', '-', 'H', '-', '-', '-', '-', '-'],
    ['W', 'W', 'H', '-', 'W', '-', '-', '-', '-', '-', '-', '-', '-', 'W', '-', 'W', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', 'W', 'W', 'W', 'H', '-', '-', '-', '-', '-', '-', 'W', '-', 'H', 'W', '-'],
    ['-', '-', '-', '-', '-', 'H', 'W', '-', '-', '-', '-', '-', '-', '-', '-', 'W', 'H', '-', '-', 'W'],
    ['W', '-', '-', '-', '-', '-', 'H', '-', 'H', '-', 'W', '-', '-', '-', '-', '-', '-', 'H', '-', '-'],
    ['-', '-', '-', '-', '-', 'W', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'H', '-'],
    ['-', 'W', '-', '-', '-', 'H', 'H', '-', 'W', '-', '-', 'W', '-', '-', '-', '-', '-', 'W', '-', '-'],
    ['-', '-', '-', '-', 'W', '-', '-', '-', '-', '-', '-', '-', 'W', '-', '-', 'W', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', 'H', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', 'H', '-', '-', 'W', '-', '-', '-', '-', 'F', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'W', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['W', 'W', '-', 'W', '-', 'H', 'W', '-', 'W', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'W', 'H', 'W', '-', '-', 'W', '-', '-'],
    ['W', '-', 'W', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'W', '-', '-', '-', '-', '-', '-']
]

binary_matrix = maze
for i in range(20):
    for j in range(20):
        if maze[i][j] == 'W':
            binary_matrix[i][j] = 0
        else:
            binary_matrix[i][j] = 1