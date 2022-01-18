from maze import binary_matrix
import heapq


def is_goal(node, end_node):
    if node == end_node:
        return 1
    return 0


def get_path(current_node):
    return [current_node[1]] + current_node[2]


def UCS(start_node, end_node):
    node_count = 0
    frontier = [(0, start_node, list(), 0)]
    heapq.heapify(frontier)
    explored = {}
    path = []

    while True:
        if len(frontier) < 1:
            print('fail')
            return 0

        state = heapq.heappop(frontier)
        if is_goal(state[1], end_node):
            return get_path(state), node_count

        explored[state[1]] = state[3]
        neighbors = list()
        (i, j) = state[1]
        for neighbor in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (i + neighbor[0], j + neighbor[1])
            if node_position[0] < 19 and node_position[0] > -1 and node_position[1] > -1 and node_position[1] < 19:
                if binary_matrix[node_position[0]][node_position[1]] > 0:
                    neighbors.append(node_position)

        for n in neighbors:
            next_cost = state[3] + 1
            if n in explored and explored[n] < next_cost:
                continue
            heapq.heappush(frontier, (next_cost, n, [state[1]] + state[2], next_cost))
            node_count += 1


(output1, node_count1) = UCS((0, 0), (3, 6))
(output2, node_count2) = UCS((3, 6), (15, 15))
print((output2 + output1[1:])[::-1])
print("node_count: ", node_count2 + node_count1)

# [(15, 15), (14, 15), (14, 14), (13, 14), (12, 14), (11, 14), (10, 14), (9, 14), (8, 14), (7, 14), (6, 14), (5, 14),
# (5, 13), (4, 13), (3, 13), (3, 12), (3, 11), (3, 10), (3, 9), (3, 8), (3, 7), (3, 6), (2, 6), (1, 6), (0, 6), (0,
# 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0)]
