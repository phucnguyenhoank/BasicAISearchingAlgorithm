
# Greedy Search uses the heuristic function to choose the node is going to be expanded
# choose the node has the lowest h(n)'s value in the current-expanding node set to expand
# there are a lot of versions of Greedy Search, in this, for for keeping simple,
# we are gonna use BFS and assume that the h(n) function is already existed
# so we just get the value of h(n) function of each node when we need

from base_modules import Searching

class GrdSearch:
    def __init__(self, problem_map, heuristic_map) -> None:
        self.problem_map = problem_map
        self.heuristic_map = heuristic_map
    
    def get_final_solution(self, start_node_name, goal_node_name):
        # determine the start node
        start_node = Searching.SearchingTreeNode(start_node_name)
        O = GreedySet(self.heuristic_map)
        O.push_right(start_node)
        expanded_node_names = set()
        while not O.is_empty():
            n = O.pop_right()

            if n.name == goal_node_name:
                return n.create_path()
            
            # expand nearby node and add it to O set
            Pn = self.problem_map.get_nearby_searching_node(n)
            expanded_node_names.add(n.name)
            for searching_node in Pn:
                if searching_node.name not in expanded_node_names:
                    O.push_right(searching_node)
        return None
    
    def print_steps(self, start_node_name, goal_node_name):
        start_node = Searching.SearchingTreeNode(start_node_name)
        O = GreedySet(self.heuristic_map)
        O.push_right(start_node)
        expanded_node_names = set()
        while not O.is_empty():
            n = O.pop_right()
            if n.father_node != None:
                print(n.name, " prior=", n.father_node.name, sep="", end="  |  ")
            else:
                print(n.name, " prior=NONE", sep="", end="  |  ")

            if n.name == goal_node_name:
                # print O set
                for searching_node in O.nodes:
                    print("(", searching_node.name, " prior=", searching_node.father_node.name, " heu=", self.heuristic_map[searching_node.name], ")", sep="", end="")
                print()
                return n.create_path()
            
            # expand nearby node and add it to O set
            Pn = self.problem_map.get_nearby_searching_node(n)
            expanded_node_names.add(n.name)
            for searching_node in Pn:
                if searching_node.name not in expanded_node_names:
                    O.push_right(searching_node)
            # print O set
            for searching_node in O.nodes:
                print("(", searching_node.name, " prior=", searching_node.father_node.name, " heu=", self.heuristic_map[searching_node.name], ")", sep="", end="")
            print()
        return None

# for private using, must have the same heuristic map with the main algorithm
# having unique node
# pop the lowest heuristic function value node
class GreedySet:
    def __init__(self, heuristic_map) -> None:
        self.nodes = list()
        self.heuristic_map = heuristic_map

    def have_node(self, searching_node):
        for node in self.nodes:
            if node.name == searching_node.name:
                return True
        return False

    def push_right(self, searching_node):
        if self.have_node(searching_node):
            return
        # create an empty place holder
        self.nodes.append(searching_node)
        i = len(self.nodes) - 2
        while i>=0 and self.heuristic_map[self.nodes[i].name] < self.heuristic_map[searching_node.name]:
            self.nodes[i+1] = self.nodes[i]
            i -= 1
        self.nodes[i+1] = searching_node
    
    def pop_right(self):
        return self.nodes.pop()

    def is_empty(self):
        if len(self.nodes) == 0:
            return True
        return False
    

    



