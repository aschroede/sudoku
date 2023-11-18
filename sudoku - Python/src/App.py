import csv
import os
from Game import Game
from Sudoku import Sudoku
from src.Heuristics.ComparableArcDomainA import ComparableArcDomainA
from src.Heuristics.ComparableArcDomainB import ComparableArcDomainB
from src.Heuristics.ComparableArcFinalized import ComparableArcFinalized
from src.Heuristics.ComparableArcOrder import ComparableArcOrder


class App:

    # Path to the Sudokus folder
    sudokus_folder = '../Sudokus'
    heuristics = [ComparableArcDomainA, ComparableArcDomainB, ComparableArcFinalized, ComparableArcOrder]

    @staticmethod
    def solve_sudoku_verbose(sudoku_file, heuristic):
        sudoku = Sudoku(sudoku_file)
        game = Game(sudoku, heuristic)

        print("Unsolved")
        game.show_sudoku()

        if game.solve() and game.valid_solution():
            print("Solved!")
        else:
            print("Could not solve this sudoku :(")

        game.show_sudoku()

        result = [game.complexity, game.num_initial_arcs_loaded, game.num_revised_arcs_loaded, game.revisions,
                  game.valid_solution()]

        print(f"Complexity: {result[0]}, Initial Arcs: {result[1]}, Added Arcs: {result[2]}, Revisions: {result[3]}, Solved: {result[4]}")

    @staticmethod
    def solve_sudoku(sudoku_file, heuristic):
        sudoku = Sudoku(sudoku_file)
        game = Game(sudoku, heuristic)
        game.solve()
        result = [game.complexity, game.num_initial_arcs_loaded, game.num_revised_arcs_loaded, game.revisions,
                  game.valid_solution()]
        return result

    @staticmethod
    def collect_data():
        data = []

        # Nicer names
        heuristic_names = ["MRV A", "MRV B", "Finalized Field", "None"]

        # Iterate over files in the Sudokus folder
        for filename in os.listdir(App.sudokus_folder):
            # Check if the file is a text file
            if filename.endswith('.txt'):
                # Iterate through heuristics
                for index, heuristic in enumerate(App.heuristics):
                    result = App.solve_sudoku(os.path.join(App.sudokus_folder, filename), heuristic)
                    row_data = [filename.split(".")[0], heuristic_names[index]]
                    row_data.extend(result)
                    data.append(row_data)

        return data

    @staticmethod
    def save_data_csv(data):
        # Save data to CSV file
        with open('sudoku_data.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(
                ['Sudoku File', 'Heuristic', 'Complexity', 'Initial Arcs', 'Added Arcs', 'Revisions', "Solved"])
            csvwriter.writerows(data)

    @staticmethod
    def start():
        while True:
            print("Select mode:")
            print("1. Data Collection Mode")
            print("2. Regular Mode")
            choice = input("Enter your choice (1 or 2): ")

            if choice == '1':
                data = App.collect_data()

                App.save_data_csv(data)

                print("Data collection completed. Results saved to sudoku_data.csv")

            elif choice == '2':
                file_num = input("Enter Sudoku file (1-5): ")
                print("Select Heuristic:")
                print("1. MRV A")
                print("2. MRV B")
                print("3. Finalized Field")
                print("4. None")
                heuristic_choice = int(input("Enter Heuristic choice (1-4): "))
                print("\n")

                file = None
                for filename in os.listdir(App.sudokus_folder):
                    # Check if the file is a text file
                    if filename.endswith('.txt') and file_num in filename:
                        file = filename

                if file is not None:
                    App.solve_sudoku_verbose(os.path.join(App.sudokus_folder, file), App.heuristics[heuristic_choice - 1])

            else:
                print("Invalid choice. Please enter 1 or 2.")

            continue_input = input("Do you want to continue? (yes/no): ")
            if continue_input.lower() != 'yes':
                break


if __name__ == "__main__":
    App.start()

