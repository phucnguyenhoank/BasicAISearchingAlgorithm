from base_modules import Searching

class UCS_Original:
    def __init__(self, problem_map) -> None:
        self.problem_map = problem_map
    
    def get_final_solution(self, start_node_name, goal_node_name):
        # determine the start node
        start_node = Searching.SearchingTreeNode(start_node_name)
        O = UCS_Set()
        O.push(start_node)
        expanded_node_names = list()
        while not O.is_empty():
            n = O.pop()
            expanded_node_names.append(n.name)
            if n.name == goal_node_name:
                return n.create_path()
            
            # expand nearby searching nodes, n-to it cost, father searching node and add it to O set
            Pn = self.problem_map.get_nearby_searching_node(n)
            for searching_node in Pn:
                if searching_node.name not in expanded_node_names:
                    searching_node.cost = n.cost + searching_node.cost # n.cost + n to searching_node cost
                    O.push(searching_node)
        return None
    
    def print_steps(self, start_node_name, goal_node_name):
        # determine the start node
        start_node = Searching.SearchingTreeNode(start_node_name)
        O = UCS_Set()
        O.push(start_node)
        expanded_node_names = list()

        while not O.is_empty():
            n = O.pop()
            expanded_node_names.append(n.name)
            if n.father_node != None:
                print(n.name, " prior=", n.father_node.name, "  |  ", sep = "", end = "")
            else:
                print(n.name, "prior=NONE", "  |  ", end = "")
            if n.name == goal_node_name:
                O.print_all_nodes()
                return n.create_path()
            
            # expand nearby searching nodes, n-to it cost, father searching node and add it to O set
            Pn = self.problem_map.get_nearby_searching_node(n)
            for searching_node in Pn:
                if searching_node.name not in expanded_node_names:
                    searching_node.cost = n.cost + searching_node.cost # n.cost + n to searching_node cost
                    O.push(searching_node)
            O.print_all_nodes()
        return None


# pop the lowest cost node
# if push already-existed node, choose the lower cost node
class UCS_Set:
    def __init__(self):
        self.nodes = list()

    def push(self, searching_node):
        searching_node_position = self.pos_of_node_name(searching_node.name)
        # if the node is already existed, replace the bigger cost node
        if searching_node_position != -1:
            if self.nodes[searching_node_position].cost > searching_node.cost:
                self.nodes.pop(searching_node_position)
            else:
                return
        # push larger cost node to the left
        # and always keep the lowest cost node to the right
        self.nodes.append(searching_node)
        i = len(self.nodes) - 2
        while i>=0 and self.nodes[i].cost < searching_node.cost:
            self.nodes[i+1] = self.nodes[i]
            i -= 1
        self.nodes[i+1] = searching_node


    def pop(self):
        return self.nodes.pop(-1)

    def pos_of_node(self, searching_node):
        for i in range(len(self.nodes)):
            if self.nodes[i].name == searching_node.name:
                return i
        return -1

    def pos_of_node_name(self, searching_node_name):
        for i in range(len(self.nodes)):
            if self.nodes[i].name == searching_node_name:
                return i
        return -1

    def is_empty(self):
        if len(self.nodes) == 0:
            return True
        return False

    def print_all(self):
        i = 0
        for node in self.nodes:
            print(node.name, node.cost, i)
            i += 1

    def print_all_nodes(self):
        for node in self.nodes:
            print("(", node.name, ",cost=", node.cost, ",prior=", node.father_node.name, ")", sep="", end="")
        print()
            
        


