
from base_modules import Searching

# NO-Checking version
class Ast:
    def __init__(self, problem_map, heuristic_function) -> None:
        self.problem_map = problem_map
        self.h = heuristic_function
    
    def get_final_solution(self, start_node_name, goal_node_name):
        # determine the start node
        start_node = Searching.SearchingTreeNode(start_node_name)
        # create A star set with an heuristic function
        O = AstSet(self.h)
        O.push_right(start_node)
        while not O.is_empty():
            # the lowest cost node is always on the right side
            n = O.pop_right()
            if n.name == goal_node_name:
                return n.create_path()
            
            # expand nearby node and add it to O set
            Pn = self.problem_map.get_nearby_searching_node(n)
            for searching_node in Pn:
                searching_node.cost = n.cost + searching_node.cost
                # let A star set decide the order of nodes
                O.push_right(searching_node)
        return None
    
    def print_steps(self, start_node_name, goal_node_name):
        # determine the start node
        start_node = Searching.SearchingTreeNode(start_node_name)
        # create A star set with an heuristic function
        O = AstSet(self.h)
        O.push_right(start_node)
        while not O.is_empty():
            n = O.pop_right()
            if n.father_node != None:
                print(n.name, " prv=", n.father_node.name, sep="", end="  |  ")
            else:
                print(n.name, " prv=NONE", sep="", end="  |  ")

            if n.name == goal_node_name:
                # print O set
                for searching_node in O.nodes:
                    print("(", searching_node.name, " prv=", searching_node.father_node.name, " f=", searching_node.cost, "+", self.h[searching_node.name], ")", sep="", end="")
                print()
                return n.create_path()
            
            # expand nearby node and add it to O set
            Pn = self.problem_map.get_nearby_searching_node(n)
            
            for searching_node in Pn:
                searching_node.cost = n.cost + searching_node.cost
                # let A star set decide the order of nodes
                O.push_right(searching_node)

            # print O set
            for searching_node in O.nodes:
                print("(", searching_node.name, " prv=", searching_node.father_node.name, " f=", searching_node.cost, "+", self.h[searching_node.name], ")", sep="", end="")
            print()
        return None

class AstSet:
    def __init__(self, heuristic_function) -> None:
        self.nodes = list()
        self.h = heuristic_function

    def is_empty(self):
        if len(self.nodes) == 0:
            return True
        return False
    
    def push_right(self, searching_node):
        # create an empty place holder
        self.nodes.append(searching_node)
        i = len(self.nodes) - 2
        while i>=0 and (self.nodes[i].cost + self.h[self.nodes[i].name]) < (searching_node.cost + self.h[searching_node.name]):
            self.nodes[i+1] = self.nodes[i]
            i -= 1
        self.nodes[i+1] = searching_node
    
    def pop_right(self):
        return self.nodes.pop()



