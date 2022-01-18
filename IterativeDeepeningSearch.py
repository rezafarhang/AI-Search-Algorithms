from GraphNode import GraphNode
from functions import action, path


class IterativeDeepeningSearch:
    def __init__(self):
        self.cutoff = 90
        self.cutoff_occured = False
        self.visited = []
        self.node_count = []

    def recursive_dls(self, node, start_node, end_node, limit):
        if node.state == end_node:
            return path(start_node, node)
        elif limit == 0:
            return self.cutoff
        else:
            cutoff_occurred = False
            # print(node.state[0], node.state[1], action(node.state[0], node.state[1]))
            if node.state not in self.visited:
                self.visited.append(node.state)
                for ac in action(node.state[0], node.state[1]):
                    child_state = None
                    if ac == 'right':
                        child_state = (node.state[0], node.state[1] + 1)
                    elif ac == 'left':
                        child_state = (node.state[0], node.state[1] - 1)
                    elif ac == 'up':
                        child_state = (node.state[0] - 1, node.state[1])
                    elif ac == 'down':
                        child_state = (node.state[0] + 1, node.state[1])

                    child_node = GraphNode(child_state, node, ac, node.cost + 1)
                    self.node_count.append(1)
                    result = self.recursive_dls(child_node, start_node, end_node, limit - 1)
                    if result == self.cutoff:
                        cutoff_occurred = True
                    elif result != 0:
                        return result
            if cutoff_occurred:
                return self.cutoff
            else:
                return 0

    def dls(self, start_node, end_node, limit):
        initial_node = GraphNode(start_node, None, None, 0)
        return self.recursive_dls(initial_node, start_node, end_node, limit)

    def ids(self, start_node, end_node, max_depth):
        for depth in range(max_depth):
            self.visited.clear()
            result = self.dls(start_node, end_node, depth)
            if result != self.cutoff:
                return result, self.node_count
            depth += 1



# obj = IterativeDeepeningSearch()
# output1, node_count1 = obj.ids((3, 6), (15, 15), 400)
# print(output1)
#

# print((output2 + output1[1:])[::-1])
# print("node_count: ", sum(node_count2) + sum(node_count1))
