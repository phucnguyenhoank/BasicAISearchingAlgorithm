from base_modules import Searching

class IDS_Original:
    def __init__(self, problem_map) -> None:
        self.problem_map = problem_map
    
    def get_final_solution(self, start_node_name, goal_node_name):
        start_node = Searching.SearchingTreeNode(start_node_name)
        O = list([start_node])
        C = 0
        while C < 50: # instead of 50, we can have 100, 200, or more
            while len(O) > 0:
                n = O.pop()
                if n.name == goal_node_name:
                    return n.create_path()
                
                # expand nearby node and add it to O set
                Pn = self.problem_map.get_nearby_searching_node(n)
                for searching_node in reversed(Pn):
                    if not n.have_on_way(searching_node) and searching_node.get_depth() <= C:
                        O.append(searching_node)
            C += 1
            O.append(start_node)
        return None
    
    def print_steps(self, start_node_name, goal_node_name):
        start_node = Searching.SearchingTreeNode(start_node_name)
        O = list([start_node])
        C = 0
        while C < 50: # instead of 50, we can have 100, 200, or more
            print("C =", C)
            while len(O) > 0:
                n = O.pop()
                if n.father_node != None:
                    print(n.name, " prior=", n.father_node.name, sep="", end="  |  ")
                else:
                    print(n.name, " prior=NONE", sep="", end="  |  ")
                if n.name == goal_node_name:
                    for searching_node in reversed(O):
                        print("(", searching_node.name, " prior=", searching_node.father_node.name, ")", sep="", end="")
                    print()
                    return n.create_path()
                
                # expand nearby node and add it to O set
                Pn = self.problem_map.get_nearby_searching_node(n)
                for searching_node in reversed(Pn):
                    if not n.have_on_way(searching_node) and searching_node.get_depth() <= C:
                        O.append(searching_node)
                        
                # print O set
                for searching_node in reversed(O):
                    print("(", searching_node.name, " prior=", searching_node.father_node.name, ")", sep="", end="")
                print()
            print("- - - - - - - - - - - - - - - - - -")
            C += 1
            O.append(start_node)

        return None