from functions import action, valid
from Queue import Queue
from GraphNode import GraphNode




def path(start_node, node: GraphNode):
    path_list = [node.state]
    while node.state != start_node:
        path_list.append(node.parent.state)
        node = node.parent
    return path_list


# node is start_node
def BFS(start_node, end_node):
    q = Queue()

    root = GraphNode(start_node, None, None, 0)

    if start_node == end_node:
        return 1

    q.enqueue(root)
    explored = []

    while True:
        if q.isempty():
            print('fail')
        node = q.dequeue()
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
            if child_node.state not in explored or q.state_exist(child_node.state):
                if child_node.state == end_node:
                    print(path(start_node, child_node))
                    return 1
                q.enqueue(child_node)


output1 = BFS((0, 0), (3, 6))
output2 = BFS((3, 6), (15, 15))
print(output2 + output1[1:])
# output1 = [(3, 6), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (3, 0), (2, 0), (1, 0), (0, 0)]
# output2 = [(15, 15), (15, 14), (15, 13), (14, 13), (13, 13), (12, 13), (11, 13), (10, 13), (10, 12), (10, 11), (9, 11),
#            (9, 10), (9, 9), (9, 8), (8, 8), (7, 8), (7, 7), (7, 6), (6, 6), (5, 6), (4, 6), (3, 6)]
# print(output2 + output1[1:])