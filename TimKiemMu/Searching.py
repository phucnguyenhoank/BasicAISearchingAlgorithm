class SearchingTreeNode:
    def __init__(self, searching_tree_node_name, come_from_start_fee = 0, father_node = None) -> None:
        self.name = searching_tree_node_name
        self.nearby_nodes = list()
        self.fee = come_from_start_fee
        self.father_node = father_node

    def add_branch(self, searching_tree_node):
        self.nearby_nodes.append(searching_tree_node)

    
    def create_path(self):
        result_path = list()
        while self.father_node != None:
            result_path.append(self.name)
            self = self.father_node
        result_path.append(self.name)
        result_path.reverse()
        return result_path
    
    def __eq__(self, other) -> bool:
        if isinstance(other, SearchingTreeNode):
            return self.name == other.name
        return False




class SearchingTree:
    pass
