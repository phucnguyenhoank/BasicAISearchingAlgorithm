from base_modules import Problem
from uninformed_search import IDS


around_s = dict(A = 55, B = 42, C = 48, E = 72)
around_a = dict(D = 45)
around_b = dict(F = 40)
around_c = dict(B = 40, F = 68, H = 73)
around_d = dict(E = 45)
around_e = dict(G = 82)
around_f = dict(G = 50)
around_h = dict(G = 60)
around_g = dict()

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



ids_original = IDS.IDS_Original(problem_map)
start_node_name = 'S'
goal_node_name = 'G'


print(ids_original.get_final_solution(start_node_name, goal_node_name))
print(ids_original.print_steps(start_node_name, goal_node_name))
