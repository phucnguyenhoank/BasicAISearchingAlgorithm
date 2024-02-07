

from base_modules import Problem
from informed_search import AStar

# Image 2.4, page 45
around_a = dict(D = 45, S = 55)
around_b = dict(C = 40, F = 40, S = 42)
around_c = dict(B = 40, F = 68, S = 48)
around_d = dict(A = 45, E = 45)
around_e = dict(D = 45, G = 82, S = 72)
around_f = dict(B = 40, C = 68, G = 55)
around_g = dict(E = 82, F = 55, I = 47, K = 38)
around_h = dict(I = 50)
around_i = dict(H = 50, G = 47)
around_k = dict(G = 38)
around_s = dict(A = 55, B = 42, C = 48, E = 72)

node_A = Problem.ProblemMapNode('A', around_a)
node_B = Problem.ProblemMapNode('B', around_b)
node_C = Problem.ProblemMapNode('C', around_c)
node_D = Problem.ProblemMapNode('D', around_d)
node_E = Problem.ProblemMapNode('E', around_e)
node_F = Problem.ProblemMapNode('F', around_f)
node_G = Problem.ProblemMapNode('G', around_g)
node_H = Problem.ProblemMapNode('H', around_h)
node_I = Problem.ProblemMapNode('I', around_i)
node_K = Problem.ProblemMapNode('K', around_k)
node_S = Problem.ProblemMapNode('S', around_s)

problem_map = Problem.ProblemMap(list((node_A, node_B, node_C, node_D, node_E, node_F, node_G, node_H, node_I, node_K, node_S)))


start_node_name = 'S'
goal_node_name = 'G'
# heuristic function for those start and goal node name
heuristic_function = dict(A = 123, B = 82, C = 118, D = 115, E = 72, F = 40, G = 0, H = 70, I = 40, K = 30, S = 125)

a_star = AStar.Ast(problem_map, heuristic_function)

# print(a_star.get_final_solution(start_node_name, goal_node_name))

print(a_star.print_steps(start_node_name, goal_node_name))
