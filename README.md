

**Implementation of Searching Algorithms in the book named 'Nhập môn trí tuệ nhân tạo - Từ Minh Phương - Học viện Công nghệ Bưu chính Viễn thông'**

### PROJECT STRUCTURE

To test an algorithm, we need to have a **ProblemMap** and a **SearchingSolution**. A **ProblemMap** can use many types of **SearchingSolution**.


#### ProblemMap

This is a class of problem map objects, which is a list of nodes called **ProblemMapNode**.

##### ProblemMapNode

Each instance of this class is a dictionary, and this dictionary contains ONLY ONE pair of key:value. The key and value are the name of the node and other name:cost pairs, which are dictionaries too.

Example of the structure of a **ProblemMapNode** and a **ProblemMap** object:

Structure of a **ProblemMapNode**:
```
nodes_around_S = dict(A = 55, B = 42, C = 48, E = 72)
ProblemMapNode_S = dict(S = nodes_around_S)
```

Structure of a **ProblemMap**:
```
ProblemMap_A = [nodeS, nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeH, nodeG]
```

Each **SearchingSolution** needs to have a **SearchingTree** and a **SearchingAlgorithm** applied on that **SearchingTree**.

#### SearchingTree

Uses pointer behavior to store its nodes, named **SearchingTreeNode**. It has a table of searching results.

##### SearchingTreeNode

Has these attributes:
- Name
- Pointers to other **SearchingTreeNode**
- Fee to arrive from the starting searching tree node
- Pointer to its father node

