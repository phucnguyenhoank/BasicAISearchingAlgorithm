class SearchingTreeNode:
    def __init__(self, searching_tree_node_name, come_from_start_cost = 0, father_node = None) -> None:
        self.name = searching_tree_node_name
        self.nearby_nodes = list()
        self.cost = come_from_start_cost
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
    
    def cost_to(self, problem_map, searching_node):
        need_to_search_node = None
        for program_map_node in problem_map.node_list:
            if program_map_node.get_name() == searching_node.name:
                need_to_search_node = program_map_node
                break
        return need_to_search_node.get_cost_to(searching_node.name)






class SearchingTree:
    pass
