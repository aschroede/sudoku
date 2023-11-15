from Game import Game
from Sudoku import Sudoku
from ComparableArcDomain import ComparableArcDomain
from ComparableArcFinalized import ComparableArcFinalized


class App:
    @staticmethod
    def start(filename):
        """
        Start AC-3 using the sudoku from the given filepath and reports whether the sudoku could be solved or not
        and how many steps it took to solve.
        @param filename:
        """

        # No heuristic
        print("=========== NO Heuristic ===========")
        heuristic = None
        sudoku = Sudoku(filename)
        game = Game(sudoku, heuristic)
        game.show_sudoku()

        if game.solve() and game.valid_solution():
            print("Solved!")
        else:
            print("Could not solve this sudoku :(")

        game.show_sudoku()
        no_heuristic_complexity = game.complexity

        # MRV
        print("=========== MRV Heuristic ===========")
        heuristic = ComparableArcDomain
        sudoku = Sudoku(filename)
        game = Game(sudoku, heuristic)
        game.show_sudoku()

        if game.solve() and game.valid_solution():
            print("Solved!")
        else:
            print("Could not solve this sudoku :(")

        game.show_sudoku()
        mrv_heuristic_complexity = game.complexity

        # Finalized
        print("=========== Finalized Field Heuristic ===========")
        heuristic = ComparableArcFinalized
        sudoku = Sudoku(filename)
        game = Game(sudoku, heuristic)
        game.show_sudoku()

        if game.solve() and game.valid_solution():
            print("Solved!")
        else:
            print("Could not solve this sudoku :(")

        game.show_sudoku()
        finalized_heuristic_complexity = game.complexity

        print(f"""
        No Heuristic: {no_heuristic_complexity}
        MRV Heuristic: {mrv_heuristic_complexity}
        Final Heuristic: {finalized_heuristic_complexity}
        """)


if __name__ == '__main__':
    # Sudoku 3, 4 can't be solved
    App.start("../Sudokus/Sudoku1.txt")
