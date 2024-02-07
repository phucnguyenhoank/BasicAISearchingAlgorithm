
from base_modules import Searching

# NO-Checking version
class IDAst:
    def __init__(self, problem_map, heuristic_function, threshold_period) -> None:
        self.problem_map = problem_map
        self.h = heuristic_function
        self.alpha = threshold_period
    
    def get_final_solution(self, start_node_name, goal_node_name):
        # determine the start node
        start_node = Searching.SearchingTreeNode(start_node_name)
        O = list([start_node])
        # create A star set with an heuristic function
        threshold = 0
        while threshold < 500: # 500 or more
            while O:
                n = O.pop()
                if n.name == goal_node_name:
                    return n.create_path()
                
                # expand nearby node and add it to O set
                Pn = self.problem_map.get_nearby_searching_node(n)
                for searching_node in reversed(Pn):
                    searching_node.cost = n.cost + searching_node.cost
                    if searching_node.cost + self.h[searching_node.name] <= threshold and not n.have_on_way(searching_node):
                        O.append(searching_node)
            threshold += self.alpha
            O.append(start_node)
        return None
    
    def print_steps(self, start_node_name, goal_node_name):
        # determine the start node
        start_node = Searching.SearchingTreeNode(start_node_name)
        O = list([start_node])
        # create A star set with an heuristic function
        threshold = 0
        while threshold < 500: # 500 or more
            print("-----------------------------------------")
            print("threshold =", threshold)
            while O:
                n = O.pop()
                if n.father_node != None:
                    print(n.name, " prv=", n.father_node.name, sep="", end="  |  ")
                else:
                    print(n.name, " prv=NONE", sep="", end="  |  ")
                if n.name == goal_node_name:
                    # print the stack
                    for searching_node in O:
                        print("(", searching_node.name, " prv=", searching_node.father_node.name, " f=", searching_node.cost, "+", self.h[searching_node.name], ")", sep="", end="")
                    print()
                    return n.create_path()
                
                # expand nearby node and add it to O set
                Pn = self.problem_map.get_nearby_searching_node(n)
                for searching_node in reversed(Pn):
                    searching_node.cost = n.cost + searching_node.cost
                    if searching_node.cost + self.h[searching_node.name] <= threshold and not n.have_on_way(searching_node):
                        O.append(searching_node)
                # print the stack
                for searching_node in O:
                    print("(", searching_node.name, " prv=", searching_node.father_node.name, " f=", searching_node.cost, "+", self.h[searching_node.name], ")", sep="", end="")
                print()
            threshold += self.alpha
            O.append(start_node)
        return None


# class IDAstSet:
#     def __init__(self, heuristic_function) -> None:
#         self.nodes = list()
#         self.h = heuristic_function

#     def is_empty(self):
#         if len(self.nodes) == 0:
#             return True
#         return False
    
#     def push_right(self, searching_node):
#         # create an empty place holder
#         self.nodes.append(searching_node)
#         i = len(self.nodes) - 2
#         while i>=0 and (self.nodes[i].cost + self.h[self.nodes[i].name]) < (searching_node.cost + self.h[searching_node.name]):
#             self.nodes[i+1] = self.nodes[i]
#             i -= 1
#         self.nodes[i+1] = searching_node
    
#     def pop_right(self):
#         return self.nodes.pop()



