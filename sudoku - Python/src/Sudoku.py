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
        # TODO: for each field, add its neighbours

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
