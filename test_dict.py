from collections import deque

def bidirectional_search(graph, start, goal):
    # two deque contains tuples, each tuple contains node name and its own path
    start_queue = deque([(start, [start])])
    goal_queue = deque([(goal, [goal])])

    # two list of visited nodes
    visited_start = set([start])
    visited_goal = set([goal])

    while start_queue and goal_queue:
        # use BFS, get current nodes and its path from two directions
        current_start, path_start = start_queue.popleft()
        current_goal, path_goal = goal_queue.popleft()

        # check if the work done
        common_nodes = set(path_start) & set(path_goal)
        if common_nodes:
            common_node_name = common_nodes.pop()
            return path_start[:path_start.index(common_node_name)] + path_goal[path_goal.index(common_node_name)::-1]

        # move to the right (to goal) from start direction
        # loop through the dictionary of neighbors
        for neighbor in graph[current_start]:
            if neighbor not in visited_start:
                # add the current node and its path for BFS
                start_queue.append((neighbor, path_start + [neighbor]))
                # mark visited
                visited_start.add(neighbor)

        # move to the left (to start) from goal direction
        for neighbor in graph[current_goal]:
            if neighbor not in visited_goal:
                goal_queue.append((neighbor, path_goal + [neighbor]))
                visited_goal.add(neighbor)

    return None  # No path found

# Example usage:
graph = {
    'S': {'A': 55, 'B': 42, 'C': 48, 'E': 72},
    'A': {'S': 55, 'D': 45},
    'B': {'S': 42, 'F': 40},
    'C': {'S': 48, 'B': 40, 'F': 68, 'H': 73},
    'D': {'A': 45, 'E': 45},
    'E': {'S': 72, 'D': 45, 'G': 82},
    'F': {'B': 40, 'C': 68, 'G': 50},
    'H': {'C': 73, 'G': 60},
    'G': {'E': 82, 'F': 50, 'H': 60}
}

start_node = 'G'
goal_node = 'A'

result = bidirectional_search(graph, start_node, goal_node)
print(result)
