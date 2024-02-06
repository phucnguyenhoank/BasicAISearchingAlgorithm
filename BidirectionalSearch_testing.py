from base_modules import Problem
from uninformed_search import BidirectionalSearch

around_s = dict(A = 55, B = 42, C = 48, E = 72)
around_a = dict(D = 45, S = 55)
around_b = dict(C = 40, F = 40, S = 42)
around_c = dict(B = 40, F = 68, H = 73, S = 48)
around_d = dict(A = 45, E = 45)
around_e = dict(G = 82, S = 72)
around_f = dict(B = 40, C = 68, G = 50)
around_h = dict(C = 73, G = 60)
around_g = dict(E = 82, F = 50, H = 60)

node_S = Problem.ProblemMapNode('S', around_s)
node_A = Problem.ProblemMapNode('A', around_a)
node_B = Problem.ProblemMapNode('B', around_b)
node_C = Problem.ProblemMapNode('C', around_c)
node_D = Problem.ProblemMapNode('D', around_d)
node_E = Problem.ProblemMapNode('E', around_e)
node_F = Problem.ProblemMapNode('F', around_f)
node_H = Problem.ProblemMapNode('H', around_h)
node_G = Problem.ProblemMapNode('G', around_g)

problem_map = Problem.ProblemMap(list((node_S, node_A, node_B, node_C, node_D, node_E, node_F, node_H, node_G)))



bds_original = BidirectionalSearch.BiDirectSearch_Original(problem_map)
start_node_name = 'A'
goal_node_name = 'G'


# print(bds_original.get_final_solution(start_node_name, goal_node_name))
print(bds_original.print_steps(start_node_name, goal_node_name))
