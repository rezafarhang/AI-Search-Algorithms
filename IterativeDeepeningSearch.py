from maze import binary_matrix
from GraphNode import GraphNode
from functions import action


def path(start_node, node: GraphNode):
    path_list = [node.state]
    while node.state != start_node:
        path_list.append(node.parent.state)
        node = node.parent
    return path_list


cutoff = 90
cutoff_occured = False

visited = []
node_count = []


def recursive_dls(node, start_node, end_node, limit):
    if node.state == end_node:
        return path(start_node, node)
    elif limit == 0:
        return cutoff
    else:
        cutoff_occurred = False
        # print(node.state[0], node.state[1], action(node.state[0], node.state[1]))
        if node.state not in visited:
            visited.append(node.state)
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
                node_count.append(1)
                result = recursive_dls(child_node, start_node, end_node, limit - 1)
                if result == cutoff:
                    cutoff_occurred = True
                elif result != 0:
                    return result
        if cutoff_occurred:
            return cutoff
        else:
            return 0


def dls(start_node, end_node, limit):
    initial_node = GraphNode(start_node, None, None, 0)
    return recursive_dls(initial_node, start_node, end_node, limit)


def ids(start_node, end_node, max_depth):
    for depth in range(max_depth):
        visited.clear()
        result = dls(start_node, end_node, depth)
        if result != cutoff:
            return (result, node_count)
        depth += 1


(output1, node_count1) = ids((0, 0), (3, 6), 400)
(output2, node_count2) = ids((3, 6), (15, 15), 400)
print((output2 + output1[1:])[::-1])

print("node_count: ", sum(node_count2) + sum(node_count1))
