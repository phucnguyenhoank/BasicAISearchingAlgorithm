from local_search import HillClimbing
# only for windows
# import winsound

number_of_queens = 10

# we can pass a N-Queen table and no repeat or not, but in here
# we don't pass N-Queen table and repeat the algorithm until find the best solution
best_improvement_hill_climbing = HillClimbing.BestImprovementHillClimbing(HillClimbing.NQueensTable(number_of_queens=number_of_queens))
best_improvement_result = best_improvement_hill_climbing.get_final_solution()

count = 0
while best_improvement_result.threating_line_number() != 0:
    best_improvement_hill_climbing = HillClimbing.BestImprovementHillClimbing(HillClimbing.NQueensTable(number_of_queens=number_of_queens))
    best_improvement_result = best_improvement_hill_climbing.get_final_solution()
    count += 1
    print('count=', count)

# winsound.Beep(440, 1000)
best_improvement_result.show_table()
print("Best improvement hill climbing done!", end='\n\n')




sto_hill_climbing = HillClimbing.StochasticHillClimbing(HillClimbing.NQueensTable(number_of_queens=number_of_queens))
sto_climbing_result = sto_hill_climbing.get_final_solution()
count = 0
while sto_climbing_result.threating_line_number() != 0:
    sto_hill_climbing = HillClimbing.StochasticHillClimbing(HillClimbing.NQueensTable(number_of_queens=number_of_queens))
    sto_climbing_result = sto_hill_climbing.get_final_solution()
    count += 1
    print('count=', count)

# winsound.Beep(440, 1000)
sto_climbing_result.show_table()
print("Stochastic hill climbing done!")

