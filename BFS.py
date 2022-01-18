from Qu import Queue
from GraphNode import GraphNode
from functions import action, path


class BFS_Search:

    def __init__(self):
        self.visited = []
        self.node_count = 0

    def BFS(self, start_node, end_node):

        q = Queue()

        root = GraphNode(start_node, None, None, 0)

        if start_node == end_node:
            return 1

        q.enqueue(root)
        explored = []

        while True:
            if q.isempty():
                print('fail')
                return 0
            node = q.dequeue()
            explored.append(node.state)

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
                    if child_node.state not in explored or q.state_exist(child_node.state):
                        if child_node.state == end_node:
                            return path(start_node, child_node), self.node_count
                        q.enqueue(child_node)
                        self.node_count += 1
