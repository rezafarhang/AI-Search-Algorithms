from BFS import BFS_Search

# BFS Algorithm

search = BFS_Search()
output1, expanded_nodes1 = search.BFS((0, 0), (3, 6))
output2, expanded_nodes2 = search.BFS((3, 6), (15, 15))

print("Traversal Path In BFS Algorithm: ", (output2 + output1[1:])[::-1])
print("Number of Expanded Node in BFS Algorithm is: ", expanded_nodes2 + expanded_nodes1)

# BFS Algorithm
