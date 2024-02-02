import Problem
import BFS

'''
CTD = 1
NTLS = 1
BDLT = 1
DHNH = 1
TTTDTTTD = 1
CDCNTD = 1
THCSLQD = 1
DHKT = 1
WMK = 1
UTE = 1
STBH = 1
NTTD = 1
'''

# TD is Thủ Đức
around_BDLT = dict(NTLS = 1, DHNH = 1)
around_NTLS = dict(BDLT = 1, TTTDTTTD = 1, CTD = 1)
around_CTD = dict(NTLS = 1, CDCNTD = 1)
around_DHNH = dict(BDLT = 1, TTTDTTTD = 1, WMK = 1)
around_TTTDTTTD = dict(NTLS = 1, DHNH = 1, THCSLQD = 1)
around_CDCNTD = dict(CTD = 1, THCSLQD = 1, DHKT = 1)
around_THCSLQD = dict(TTTDTTTD = 1, CDCNTD = 1, DHKT = 1, UTE = 1)
around_DHKT = dict(CDCNTD = 1, THCSLQD = 1, STBH = 1)
around_WMK = dict(DHNH = 1, NTTD = 1)
around_UTE = dict(THCSLQD = 1, NTTD = 1)
around_NTTD = dict(WMK = 1, UTE = 1, STBH = 1)
around_STBH = dict(DHKT = 1, NTTD = 1)

node_A = Problem.ProblemMapNode('BDLT', around_BDLT)
node_B = Problem.ProblemMapNode('NTLS', around_NTLS)
node_C = Problem.ProblemMapNode('CTD', around_CTD)
node_D = Problem.ProblemMapNode('DHNH', around_DHNH)
node_E = Problem.ProblemMapNode('TTTDTTTD', around_TTTDTTTD)
node_F = Problem.ProblemMapNode('CDCNTD', around_CDCNTD)
node_G = Problem.ProblemMapNode('THCSLQD', around_THCSLQD)
node_H = Problem.ProblemMapNode('DHKT', around_DHKT)
node_I = Problem.ProblemMapNode('WMK', around_WMK)
node_J = Problem.ProblemMapNode('UTE', around_UTE)
node_K = Problem.ProblemMapNode('STBH', around_STBH)
node_L = Problem.ProblemMapNode('NTTD', around_NTTD)



problem_map = Problem.ProblemMap(list((node_A, node_B, node_C, node_D, node_E, node_F, node_G, node_H, node_I, node_J, node_K, node_L)))

bfs_original = BFS.BFS_Original(problem_map)
bfs_check_expanded = BFS.BFS_CheckExpanded(problem_map)
bfs_check_goal_before_add = BFS.BFS_CheckGoalBeforeAdd(problem_map)
bfs_optimize = BFS.BFS_Optimize(problem_map)

start_node_name = 'BDLT'
goal_node_name = 'STBH'
print(bfs_original.print_steps(start_node_name, goal_node_name))
print("----------------------------------------------")
print(bfs_check_expanded.print_steps(start_node_name, goal_node_name))
print("----------------------------------------------")
print(bfs_check_goal_before_add.print_steps(start_node_name, goal_node_name))
print("----------------------------------------------")
print(bfs_optimize.print_steps(start_node_name, goal_node_name))






