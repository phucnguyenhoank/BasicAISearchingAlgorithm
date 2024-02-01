
# nearby in here is different, 
# nearby nodes of A are nodes A can go

import Searching

class ProblemMapNode:
    def __init__(self, name, nearby_roads):
        self.node = dict()
        self.node[name] = nearby_roads

    def get_name(self):
        return list(self.node.keys())[0]
    
    def get_cost_to(self, nearby_node_name):
        nearby_roads = self.node[self.get_name()]
        for nearby_road_name in nearby_roads.keys():
            if nearby_road_name == nearby_node_name:
                return nearby_roads[nearby_road_name]
        return 0
    
    def get_nearby_node_names(self):
        nearby_node_names = list()
        nearby_roads = self.node[self.get_name()]
        return list(nearby_roads.keys())




class ProblemMap:
    def __init__(self, problem_map_nodes) -> None:
        self.node_list = problem_map_nodes

    def get_nearby_nodes(self, node_name):
        # looking for the node which we need to search around it
        need_to_search_node = None
        for program_map_node in self.node_list:
            if program_map_node.get_name() == node_name:
                need_to_search_node = program_map_node
                break
        
        nearby_node_names = need_to_search_node.get_nearby_node_names()

        nearby_nodes = list()
        for program_map_node in self.node_list:
            if program_map_node.get_name() in nearby_node_names:
                nearby_nodes.append(program_map_node)

        return nearby_nodes

    # without parent and fee
    def get_nearby_searching_node(self, searching_node):
        need_to_search_node = None
        for program_map_node in self.node_list:
            if program_map_node.get_name() == searching_node.name:
                need_to_search_node = program_map_node
                break
        nearby_node_names = need_to_search_node.get_nearby_node_names()

        searching_nodes = list()
        for name in nearby_node_names:
            searching_nodes.append(Searching.SearchingTreeNode(name))
        
        return searching_nodes













    

    


