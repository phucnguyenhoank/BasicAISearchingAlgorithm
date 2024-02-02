
import Searching
import queue

class BFS_Original:
    def __init__(self, problem_map) -> None:
        self.problem_map = problem_map
    
    def get_final_solution(self, start_node_name, goal_node_name):
        # determine the start node
        start_node = Searching.SearchingTreeNode(start_node_name)
        O = queue.Queue()
        O.put(start_node)
        while not O.empty():
            n = O.get()

            if n.name == goal_node_name:
                return n.create_path()
            
            # expand nearby node and add it to O set
            Pn = self.problem_map.get_nearby_searching_node(n)
            for searching_node in Pn:
                searching_node.father_node = n
                O.put(searching_node)
        return None
    
    def print_steps(self, start_node_name, goal_node_name):
        start_node = Searching.SearchingTreeNode(start_node_name)
        O = queue.Queue()
        O.put(start_node)
        # create a name list contains all names of current nodes in the O set with the same order
        expandable_node_names = list([start_node.name])
        while not O.empty():
            n = O.get()
            print(expandable_node_names.pop(0), "  |  ", end = "")

            if n.name == goal_node_name:
                print(", ".join(expandable_node_names))
                return n.create_path()
            
            Pn = self.problem_map.get_nearby_searching_node(n)
            for searching_node in Pn:
                searching_node.father_node = n
                O.put(searching_node)
                expandable_node_names.append(searching_node.name)
            print(", ".join(expandable_node_names))
        return None



class BFS_CheckExpanded:
    def __init__(self, problem_map) -> None:
        self.problem_map = problem_map
    
    def get_final_solution(self, start_node_name, goal_node_name):
        # determine the start node
        start_node = Searching.SearchingTreeNode(start_node_name)
        O = queue.Queue()
        O.put(start_node)
        expanded_node_names = list()
        while not O.empty():
            n = O.get()
            expanded_node_names.append(n.name)
            if n.name == goal_node_name:
                return n.create_path()
            
            # expand nearby node and add it to O set
            Pn = self.problem_map.get_nearby_searching_node(n)
            for searching_node in Pn:
                if searching_node not in O.queue and searching_node.name not in expanded_node_names:
                    searching_node.father_node = n
                    O.put(searching_node)
        return None
    
    def print_steps(self, start_node_name, goal_node_name):
        # determine the start node
        start_node = Searching.SearchingTreeNode(start_node_name)
        O = queue.Queue()
        O.put(start_node)
        expanded_node_names = list()
        expandable_node_names = list([start_node.name])
        while not O.empty():
            n = O.get()
            expanded_node_names.append(n.name)
            print(expandable_node_names.pop(0), "  |  ", end = "")
            if n.name == goal_node_name:
                print(", ".join(expandable_node_names))
                return n.create_path()
            
            # expand nearby node and add it to O set
            Pn = self.problem_map.get_nearby_searching_node(n)
            for searching_node in Pn:
                if searching_node not in O.queue and searching_node.name not in expanded_node_names:
                    searching_node.father_node = n
                    O.put(searching_node)
                    expandable_node_names.append(searching_node.name)
            print(", ".join(expandable_node_names))
        return None



class BFS_CheckGoalBeforeAdd:
    def __init__(self, problem_map) -> None:
        self.problem_map = problem_map
    
    def get_final_solution(self, start_node_name, goal_node_name):
        start_node = Searching.SearchingTreeNode(start_node_name)
        if start_node.name == goal_node_name:
            return start_node_name.create_path()
        O = queue.Queue()
        O.put(start_node)
        while not O.empty():
            n = O.get()
            Pn = self.problem_map.get_nearby_searching_node(n)
            for searching_node in Pn:
                searching_node.father_node = n
                if searching_node.name == goal_node_name:
                    return searching_node.create_path()
                O.put(searching_node)       
        return None
    
    def print_steps(self, start_node_name, goal_node_name):
        start_node = Searching.SearchingTreeNode(start_node_name)
        if start_node.name == goal_node_name:
            return start_node_name.create_path()
        O = queue.Queue()
        O.put(start_node)
        expandable_node_names = list([start_node.name])
        while not O.empty():
            n = O.get()
            print(expandable_node_names.pop(0), "  |  ", end = "")

            Pn = self.problem_map.get_nearby_searching_node(n)
            for searching_node in Pn:
                searching_node.father_node = n
                if searching_node.name == goal_node_name:
                    print(", ".join(expandable_node_names))
                    return searching_node.create_path()
                O.put(searching_node)
                expandable_node_names.append(searching_node.name)
            print(", ".join(expandable_node_names))       
        return None




class BFS_Optimize:
    def __init__(self, problem_map) -> None:
        self.problem_map = problem_map
    
    def get_final_solution(self, start_node_name, goal_node_name):
        start_node = Searching.SearchingTreeNode(start_node_name)
        if start_node.name == goal_node_name:
            return start_node_name.create_path()
        O = queue.Queue()
        O.put(start_node)
        expanded_node_names = list()
        while not O.empty():
            n = O.get()
            Pn = self.problem_map.get_nearby_searching_node(n)
            expanded_node_names.append(n.name)
            for searching_node in Pn:
                searching_node.father_node = n
                if searching_node.name == goal_node_name:
                    return searching_node.create_path()
                elif searching_node not in O.queue and searching_node.name not in expanded_node_names:
                    O.put(searching_node)
        return None
    
    def print_steps(self, start_node_name, goal_node_name):
        start_node = Searching.SearchingTreeNode(start_node_name)
        if start_node.name == goal_node_name:
            return start_node_name.create_path()
        O = queue.Queue()
        O.put(start_node)
        expanded_node_names = list()
        expandable_node_names = list([start_node.name])
        while not O.empty():
            n = O.get()
            Pn = self.problem_map.get_nearby_searching_node(n)
            expanded_node_names.append(n.name)
            print(expandable_node_names.pop(0), "  |  ", end = "")

            for searching_node in Pn:
                searching_node.father_node = n
                if searching_node.name == goal_node_name:
                    print(", ".join(expandable_node_names))
                    return searching_node.create_path()
                elif searching_node not in O.queue and searching_node.name not in expanded_node_names:
                    O.put(searching_node)
                    expandable_node_names.append(searching_node.name)
            print(", ".join(expandable_node_names))
        return None






