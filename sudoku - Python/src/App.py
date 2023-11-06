from Game import Game
from Sudoku import Sudoku


class App:
    @staticmethod
    def start(filename):
        """
        Start AC-3 using the sudoku from the given filepath and reports whether the sudoku could be solved or not
        and how many steps it took to solve.
        @param filename:
        """
        game = Game(Sudoku(filename))
        game.show_sudoku()

        if game.solve() and game.validSolution():
            print("Solved!")
        else:
            print("Could not solve this sudoku :(")

        game.show_sudoku()


if __name__ == '__main__':
    App.start("../Sudokus/Sudoku2.txt")