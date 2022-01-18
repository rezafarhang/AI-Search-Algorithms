from BFS import BFS_Search
from IterativeDeepeningSearch import IterativeDeepeningSearch
from UniformCostSearch import UniformCostSearch
from Astar import AstarSearch

# BFS Algorithm

search = BFS_Search()
output1, expanded_nodes1 = search.BFS((0, 0), (3, 6))
output2, expanded_nodes2 = search.BFS((3, 6), (15, 15))

print("Traversal Path In BFS Algorithm: ", (output2 + output1[1:])[::-1])
print("Number of Expanded Node in BFS Algorithm is: ", expanded_nodes2 + expanded_nodes1)
print()

# BFS Algorithm

# IDDFS Algorithm

search = IterativeDeepeningSearch()
output1, expanded_nodes1 = search.ids((0, 0), (3, 6), 400)
output2, expanded_nodes2 = search.ids((3, 6), (15, 15), 400)

print("Traversal Path In IDDFS Algorithm: ", (output2 + output1[1:])[::-1])
print("Number of Expanded Node in IDDFS Algorithm is: ", sum(expanded_nodes2) + sum(expanded_nodes1))
print()

# IDDFS Algorithm

# UCS

search = UniformCostSearch()
output1, expanded_nodes1 = search.UCS((0, 0), (3, 6))
output2, expanded_nodes2 = search.UCS((3, 6), (15, 15))

print("Traversal Path In UCS Algorithm: ", (output2 + output1[1:])[::-1])
print("Number of Expanded Node in UCS Algorithm is: ", expanded_nodes2 + expanded_nodes1)
print()

# UCS

# A Star

search = AstarSearch()
output1, expanded_nodes1 = search.a_star((0, 0), (3, 6))
output2, expanded_nodes2 = search.a_star((3, 6), (15, 15))

print("Traversal Path In A star Algorithm: ", (output2 + output1[1:])[::-1])
print("Number of Expanded Node in A star Algorithm is: ", expanded_nodes2 + expanded_nodes1)
# print("node_count: ", sum(node_count2) + sum(node_count1))

# A Star
