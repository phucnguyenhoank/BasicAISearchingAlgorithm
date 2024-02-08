import random
import copy

# for specifying, we will implement this algorithm using N-Queen problem and NO repetition
class BestImprovementHillClimbing:
    def __init__(self, N_queen_table = None) -> None:
        if N_queen_table == None:
            self.n_queen_problem = NQueensTable()
        else:
            self.n_queen_problem = N_queen_table 

    def get_final_solution(self):
        # init the first state
        current_queen_table = copy.deepcopy(self.n_queen_problem)
        while True:
            have_better = False
            for new_table in current_queen_table.one_move_neighbors():
                if new_table.threating_line_number() < current_queen_table.threating_line_number():
                    have_better = True
                    current_queen_table = new_table
            if have_better == False:
                return current_queen_table


class StochasticHillClimbing:
    def __init__(self, N_queen_table = None) -> None:
        if N_queen_table == None:
            self.n_queen_problem = NQueensTable()
        else:
            self.n_queen_problem = N_queen_table 

    def get_final_solution(self):
        # init the first state
        current_queen_table = copy.deepcopy(self.n_queen_problem)
        while True:
            neighbors = current_queen_table.one_move_neighbors()
            new_table = random.choice(neighbors)
            patience = 0
            while patience < 100 and new_table.threating_line_number() >= current_queen_table.threating_line_number():
                new_table = random.choice(neighbors)
                patience += 1
                
            if patience == 100:
                return current_queen_table
            else:
                current_queen_table = new_table

class NQueensTable:
    # one column contains only one queen
    # the the rows and columns are numbered from 1 to 8, from left to right, and from bottom to top
    # each queen in the 'queens' list are queens in each column
    # the value in each element of the list is the number of the row respectively
    # the index of the queens list starts from 1
    def __init__(self, queens = None, number_of_queens = 8) -> None:
        if queens == None:
            self.queens = [random.randint(1, number_of_queens) for _ in range(number_of_queens + 1)]
            self.queen_number = number_of_queens
        else:
            self.queens = queens
            self.queen_number = len(queens) - 1

    def have_queen(self, row, col):
        if self.queens[col] == row:
            return True
        return False

    def get_pos_queen_at_column(self, col):
        return self.queens[col], col

    def threating_line_number(self):
        threating_line_number = 0
        queen_at = 1
        while queen_at <= self.queen_number:
            x, y = self.get_pos_queen_at_column(queen_at)

            # check vertical
            row_queen_counter = 0
            for row_number in range(1, self.queen_number + 1):
                if self.have_queen(row_number, y):
                    row_queen_counter += 1
            row_queen_counter -= 1

            # check horizon
            col_queen_counter = 0
            for col_number in range(1, self.queen_number + 1):
                if self.have_queen(x, col_number):
                    col_queen_counter += 1
            col_queen_counter -= 1

            # check diagonal
            # \ direction
            diagonal_counter = 0
            temp_x = x
            temp_y = y
            while temp_x <= self.queen_number and temp_y <= self.queen_number:
                if self.have_queen(temp_x, temp_y):
                    diagonal_counter += 1
                temp_x += 1
                temp_y += 1
            
            temp_x = x
            temp_y = y
            while temp_x >= 1 and temp_y >= 1:
                if self.have_queen(temp_x, temp_y):
                    diagonal_counter += 1
                temp_x -= 1
                temp_y -= 1
            # / direction
            temp_x = x
            temp_y = y
            while temp_x <= self.queen_number and temp_y >= 1:
                if self.have_queen(temp_x, temp_y):
                    diagonal_counter += 1
                temp_x += 1
                temp_y -= 1

            temp_x = x
            temp_y = y
            while temp_x >= 1 and temp_y <= self.queen_number:
                if self.have_queen(temp_x, temp_y):
                    diagonal_counter += 1
                temp_x -= 1
                temp_y += 1
            # minus the recount place
            diagonal_counter -= 4

            threating_line_number += row_queen_counter + col_queen_counter + diagonal_counter
            queen_at += 1
        return threating_line_number

    def show_table(self):
        for i in range(self.queen_number, 0, -1):
            for j in range(1, self.queen_number + 1):
                if self.have_queen(i, j):
                    print("Q", end = " ")
                else:
                    print(".", end = " ")
            print()

    def move_one_queen(self):
        selected_column = random.randint(1, 8)
        selected_new_row = random.randint(1, 8)
        while selected_new_row == self.queens[selected_column]:
            selected_new_row = random.randint(1, 8)
        self.queens[selected_column] = selected_new_row
    
    def move_two_queen(self):
        # move the first column
        selected_column_a = random.randint(1, 8)
        selected_new_row = random.randint(1, 8)
        while selected_new_row == self.queens[selected_column_a]:
            selected_new_row = random.randint(1, 8)
        self.queens[selected_column_a] = selected_new_row

        # move the second column
        selected_column_b = random.randint(1, 8)
        while selected_column_b == selected_column_a:
            selected_column_b = random.randint(1, 8)
        selected_new_row = random.randint(1, 8)
        while selected_new_row == self.queens[selected_column_b]:
            selected_new_row = random.randint(1, 8)
        self.queens[selected_column_b] = selected_new_row

    # return a list of all possible ways when we move a queen
    def one_move_neighbors(self):
        one_move_neighbor_tables = list()
        
        for selected_column in range(1, self.queen_number + 1):
            
            old_row = self.queens[selected_column]
            for new_row in range(1, self.queen_number + 1):
                if new_row != old_row:
                    clone_queens = list(self.queens)
                    clone_queens[selected_column] = new_row
                    one_move_neighbor_tables.append(NQueensTable(clone_queens))
        
        return one_move_neighbor_tables


