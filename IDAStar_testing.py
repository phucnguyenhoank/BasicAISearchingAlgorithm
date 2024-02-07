
from base_modules import Problem
from informed_search import IDAStar

# Image 2.16, page 51
around_a = dict(D = 3)
around_b = dict(C = 3, D = 1)
around_c = dict(E = 2)
around_d = dict(C = 1, F = 3)
around_e = dict(G = 1)
around_f = dict(G = 2)
around_g = dict()
around_s = dict(A = 2, B = 3)

node_A = Problem.ProblemMapNode('A', around_a)
node_B = Problem.ProblemMapNode('B', around_b)
node_C = Problem.ProblemMapNode('C', around_c)
node_D = Problem.ProblemMapNode('D', around_d)
node_E = Problem.ProblemMapNode('E', around_e)
node_F = Problem.ProblemMapNode('F', around_f)
node_G = Problem.ProblemMapNode('G', around_g)
node_S = Problem.ProblemMapNode('S', around_s)

problem_map = Problem.ProblemMap(list((node_A, node_B, node_C, node_D, node_E, node_F, node_G, node_S)))


start_node_name = 'S'
goal_node_name = 'G'
# heuristic function for those start and goal node name
heuristic_function = dict(A = 4, B = 4, C = 3, D = 4, E = 1, F = 1, G = 0, S = 6)

ida_star = IDAStar.IDAst(problem_map, heuristic_function, 2)
# ida_star_2 = IDAStar.IDAst(problem_map, heuristic_function, 3)


# print(ida_star.get_final_solution(start_node_name, goal_node_name))
print(ida_star.print_steps(start_node_name, goal_node_name))
