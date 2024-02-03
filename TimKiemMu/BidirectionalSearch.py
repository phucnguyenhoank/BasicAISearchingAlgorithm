import Searching
import collections

class BiDirectSearch_Original:
    def __init__(self, problem_map) -> None:
        self.problem_map = problem_map


    def get_final_solution(self, start_node_name, goal_node_name):
        # use BFS for the two direction
        # create two queue
        # one begins from start
        start_queue = collections.deque([Searching.SearchingTreeNode(start_node_name)])
        # one begins from goal
        goal_queue = collections.deque([Searching.SearchingTreeNode(goal_node_name)])

        # for a little bit BFS optimize
        visited_searching_nodes_start = set([start_node_name])
        visited_searching_nodes_goal = set([goal_node_name])

        while start_queue or goal_queue:
            if start_queue:
                from_start_node = start_queue.popleft()
            if goal_queue:
                from_goal_node = goal_queue.popleft()

            # check if there are any common visited node
            start_node_path = from_start_node.create_path()
            goal_node_path = from_goal_node.create_path()
            common_nodes = set(start_node_path) & set(goal_node_path)
            if common_nodes:
                common_node_name = common_nodes.pop()
                return start_node_path[:start_node_path.index(common_node_name)] + goal_node_path[goal_node_path.index(common_node_name)::-1]

            # expand from start direction
            start_Pn = self.problem_map.get_nearby_searching_node(from_start_node)
            for searching_node in start_Pn:
                if searching_node not in start_queue and searching_node.name not in visited_searching_nodes_start:
                    start_queue.append(searching_node)

            # expand from goal direction
            goal_Pn = self.problem_map.get_nearby_searching_node(from_goal_node)
            for searching_node in goal_Pn:
                if searching_node not in goal_queue and searching_node.name not in visited_searching_nodes_goal:
                    goal_queue.append(searching_node)
        return None



        


    def print_steps(self, start_node_name, goal_node_name):
        # use BFS for the two direction
        # create two queue
        # one begins from start
        start_queue = collections.deque([Searching.SearchingTreeNode(start_node_name)])
        # one begins from goal
        goal_queue = collections.deque([Searching.SearchingTreeNode(goal_node_name)])

        # for a little bit BFS optimize
        visited_searching_nodes_start = set([start_node_name])
        visited_searching_nodes_goal = set([goal_node_name])

        while start_queue or goal_queue:
            if start_queue:
                from_start_node = start_queue.popleft()
                print("from start direction node: ", end='')
                if from_start_node.father_node != None:
                    print(from_start_node.name, " prior=", from_start_node.father_node.name, sep="")
                else:
                    print(from_start_node.name, " prior=NONE", sep="")
            if goal_queue:
                from_goal_node = goal_queue.popleft()
                print("from goal direction node: ", end='')
                if from_goal_node.father_node != None:
                    print(from_goal_node.name, " prior=", from_goal_node.father_node.name, sep="")
                else:
                    print(from_goal_node.name, " prior=NONE", sep="")

            
            # check if there are any common visited node
            start_node_path = from_start_node.create_path()
            goal_node_path = from_goal_node.create_path()
            print(start_node_path)
            print(goal_node_path)
            common_nodes = set(start_node_path) & set(goal_node_path)
            if common_nodes:
                common_node_name = common_nodes.pop()
                print('have common node:', common_node_name)
                return start_node_path[:start_node_path.index(common_node_name)] + goal_node_path[goal_node_path.index(common_node_name)::-1]

            # expand from start direction
            start_Pn = self.problem_map.get_nearby_searching_node(from_start_node)
            for searching_node in start_Pn:
                if searching_node not in start_queue and searching_node.name not in visited_searching_nodes_start:
                    start_queue.append(searching_node)
            

            # expand from goal direction
            goal_Pn = self.problem_map.get_nearby_searching_node(from_goal_node)
            for searching_node in goal_Pn:
                if searching_node not in goal_queue and searching_node.name not in visited_searching_nodes_goal:
                    goal_queue.append(searching_node)

            # print queue
            print("start queue: ", end='')
            for searching_node in start_queue:
                print("(", searching_node.name, " prior=", searching_node.father_node.name, ")", sep="", end="")
            print()
            print("goal queue: ", end='')
            for searching_node in goal_queue:
                print("(", searching_node.name, " prior=", searching_node.father_node.name, ")", sep="", end="")
            print()
            print()

        return None
