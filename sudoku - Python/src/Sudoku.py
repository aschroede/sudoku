import math

from Field import Field


class Sudoku:

    def __init__(self, filename):
        self.board = self.read_sudoku(filename)

    def __str__(self):

        output = "╔═══════╦═══════╦═══════╗\n"

        # iterate through rows
        for i in range(9):
            if i == 3 or i == 6:
                output += "╠═══════╬═══════╬═══════╣\n"

            output += "║ "

            # iterate through columns
            for j in range(9):
                if j == 3 or j == 6:
                    output += "║ "
                output += str(self.board[i][j]) + " "

            output += "║\n"

        output += "╚═══════╩═══════╩═══════╝\n"

        return output

    @staticmethod
    def read_sudoku(filename):
        assert filename is not None and filename != "", "Invalid filename"

        grid = [[Field for _ in range(9)] for _ in range(9)]

        try:
            with open(filename, "r") as file:
                for row_index, line in enumerate(file):
                    for col_index, char in enumerate(line):
                        if char == '\n':
                            continue
                        if int(char) == 0:
                            grid[row_index][col_index] = Field()
                        else:
                            grid[row_index][col_index] = Field(int(char))

        except FileNotFoundError:
            print("Error opening file: " + filename)

        Sudoku.add_neighbours(grid)
        return grid

    @staticmethod
    def add_neighbours(grid):
        """
        Adds a list of neighbors to each field
        @param grid:
        """

        # Start by iterating over each of the fields

        for row in range(len(grid)):

            for col in range(len(grid[row])):
                # Add all neighbors in same row

                # Just append all neighbors to same list, don't think it matters wether the neighbor
                # came from a row, column, or box. But if it does end up mattering in the future you
                # can store each of these sets of neighbors in their own list inside a larger list.
                all_neighbors = []
                all_neighbors += Sudoku.get_row_neighbors(grid, row, col)
                all_neighbors += Sudoku.get_col_neighbors(grid, row, col)
                all_neighbors += Sudoku.get_box_neighbors(grid, row, col)

                my_neighbor_set = set(all_neighbors)

                grid[row][col].set_neighbours(my_neighbor_set)

    @staticmethod
    def get_row_neighbors(grid, row, col):

        neighbors = []
        for i in range(len(grid)):
            if i != col:
                neighbors.append(grid[row][i])
        return neighbors

    @staticmethod
    def get_col_neighbors(grid, row, col):

        neighbors = []
        for i in range(len(grid)):
            if i != row:
                neighbors.append(grid[i][col])
        return neighbors

    @staticmethod
    def get_box_neighbors(grid, row, col):

        start_row_range = math.floor(row / 3) * 3
        start_col_range = math.floor(col / 3) * 3

        neighbors = []

        for r in range(start_row_range, start_row_range + 3):
            for c in range(start_col_range, start_col_range + 3):

                if not (r == row and c == col):
                    neighbors.append(grid[r][c])

        return neighbors

    def board_to_string(self):

        output = ""
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                output += self.board[row][col].get_value()
            output += "\n"
        return output

    def get_board(self):
        self.self_board = self.board
        return self.self_board
