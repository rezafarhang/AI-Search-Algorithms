from GraphNode import GraphNode
from Qu import Queue
from functions import action, path


def ucs(start_node, end_node):
    root = GraphNode(start_node, None, None, 0)
    frontier = Queue()
    frontier.enqueue(root)
    explored = []

    while True:
        if frontier.isempty():
            return 'failure'
        node = frontier.dequeue()
        if node.state == end_node:
            print(path(start_node, node))
            return 1
        explored.append(node.state)
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
            if child_node.state not in explored or frontier.state_exist(child_node.state):
                frontier.enqueue(child_node)
                frontier.queue.sort(key=lambda x: x.cost)
            elif child_node.state in explored:
                # for nod in frontier.queue:
                #     if nod.state == child_node.state:
                #         if node.cost > child_node.cost:
                #             frontier.queue.remove(nod)
                #             frontier.enqueue(child_node)


ucs((0, 0), (3, 6))
ucs((3, 6), (15, 15))
