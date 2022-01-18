from BFS import BFS_Search
from IterativeDeepeningSearch import IterativeDeepeningSearch

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
