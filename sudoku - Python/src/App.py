from Game import Game
from Sudoku import Sudoku
from src.Heuristics.ComparableArcDomainA import ComparableArcDomainA
from src.Heuristics.ComparableArcDomainB import ComparableArcDomainB
from src.Heuristics.ComparableArcFinalized import ComparableArcFinalized
from src.Heuristics.ComparableArcOrder import ComparableArcOrder


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
        heuristic = ComparableArcOrder
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
        print("=========== MRV Heuristic A ===========")
        heuristic = ComparableArcDomainA
        sudoku = Sudoku(filename)
        game = Game(sudoku, heuristic)
        game.show_sudoku()

        if game.solve() and game.valid_solution():
            print("Solved!")
        else:
            print("Could not solve this sudoku :(")

        game.show_sudoku()
        mrv_heuristicA_complexity = game.complexity

        # MRV
        print("=========== MRV Heuristic B ===========")
        heuristic = ComparableArcDomainB
        sudoku = Sudoku(filename)
        game = Game(sudoku, heuristic)
        game.show_sudoku()

        if game.solve() and game.valid_solution():
            print("Solved!")
        else:
            print("Could not solve this sudoku :(")

        game.show_sudoku()
        mrv_heuristicB_complexity = game.complexity

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
        MRV HeuristicA: {mrv_heuristicA_complexity}
        MRV HeuristicB: {mrv_heuristicB_complexity}
        Final Heuristic: {finalized_heuristic_complexity}
        """)


if __name__ == '__main__':
    # Sudoku 3, 4 can't be solved
    App.start("../Sudokus/Sudoku5.txt")
