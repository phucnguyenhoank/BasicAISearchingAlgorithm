Implementation of searching Algorithms in the book named 'Nhập môn trí tuệ nhân tạo - Từ Minh Phương - Học viện Công nghệ Bưu chính Viễn thông'



PROJECT STRUCTURE

To testing an algorithm, we need to have a ProblemMap and a SearchingSolution
ProblemMap and use many type of SearchingSolution.

===============================================================================================
ProblemMap 
This is a class of problem map objects,
which is a list nodes called ProblemMapNode.

ProblemMapNode
Each instance of this class is a dictionary, this dictionary contains ONLY ONE pair of key:value
key and value are the name of the node and other name:cost pairs, which are dictionaries too.

Example of structure of a ProblemMapNode and a ProblemMap objects:
this is a structure of a ProblemMapNode
nodes_around_S = dict(A = 55, B = 42, C = 48, E = 72)
ProblemMapNode_S = dict(S = nodes_around_S)

this is a structure of a ProblemMap
ProblemMap_A = [nodeS, nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeH, nodeG]


===============================================================================================
Each SearchingSolution need to have a SearchingTree and an SearchingAlgorithm applied on that searching SearchingTree

SearchingTree
Use pointer behavior to stores its nodes, named SearchingTreeNode
Has a table of searching result

SearchingTreeNode
Has these attributes:
- Name
- Pointers to other SearchingTreeNode
- Fee to arrive from starting searching tree node
- Pointer to its father node




