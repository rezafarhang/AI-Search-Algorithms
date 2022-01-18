from maze import binary_matrix
from functions import is_goal, get_path
from math import sqrt
import heapq


class AstarSearch:
    def __init__(self):
        self.explored = {}

    def heuristic(self, node, end_node):
        x = node[0]
        y = node[1]
        return round(sqrt((abs(x - end_node[0])) ** 2 + (abs(y - end_node[1])) ** 2))

    def a_star(self, start_node, end_node):
        node_count = 0
        frontier = [(self.heuristic(start_node, end_node), start_node, list(), 0)]
        heapq.heapify(frontier)

        while True:
            if len(frontier) < 1:
                print('fail')
                return 0

            state = heapq.heappop(frontier)
            if is_goal(state[1], end_node):
                return get_path(state), node_count

            self.explored[state[1]] = state[3]
            neighbors = list()
            (i, j) = state[1]
            for neighbor in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                node_position = (i + neighbor[0], j + neighbor[1])
                if 19 > node_position[0] > -1 and -1 < node_position[1] < 19:
                    if binary_matrix[node_position[0]][node_position[1]] > 0:
                        neighbors.append(node_position)

            for n in neighbors:
                next_cost = state[3] + 1
                if n in self.explored and self.explored[n] < next_cost:
                    continue
                heapq.heappush(frontier, (self.heuristic(n, end_node) + next_cost, n, [state[1]] + state[2], next_cost))
                node_count += 1