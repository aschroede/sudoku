from collections import deque
from queue import PriorityQueue
from OrderedPriorityQueue import OrderedPriorityQueue
from Arc import Arc


class Game:

    def __init__(self, sudoku, heuristic):
        self.sudoku = sudoku
        self.complexity = 0
        self.revisions = 0
        self.addqueuenum = 0
        self.priority_queue = OrderedPriorityQueue() if heuristic is None else PriorityQueue()
        self.heuristic = heuristic

    def show_sudoku(self):
        print(self.sudoku)

    def solve(self):
        """
        Implementation of the AC-3 algorithm
        @return: true if the constraints can be satisfied, false otherwise
        """
        self.load_arcs()

        while not self.priority_queue.empty():

            # Increment complexity measure
            self.complexity += 1

            arc = self.priority_queue.get()

            if not arc.m.is_finalized():

                domain_changed = self.revise(arc)

                if arc.m.get_domain_size() == 0 and arc.m.get_value() == 0:
                    return False

                if domain_changed:

                    for neighbor in arc.m.get_other_neighbours(arc.n):

                        if not neighbor.is_finalized():

                            if self.heuristic is None:
                                new_arc = Arc(neighbor, arc.m)
                            else:
                                new_arc = self.heuristic(neighbor, arc.m)

                            if new_arc not in self.priority_queue.queue:
                                self.addqueuenum += 1
                                self.priority_queue.put(new_arc)

        print("Number of revisions: " + str(self.revisions))
        print("Number of added arcs: " + str(self.addqueuenum))

        return True

    def revise(self, arc):

        domain_changed = False

        # Only restrict domain if value of neighbor is finalized
        if arc.n.is_finalized():
            for value in arc.m.get_domain():
                if value == arc.n.get_value():
                    self.revisions += 1
                    domain_changed = True
                    arc.m.remove_from_domain(value)

        return domain_changed

    def load_arcs(self):
        num_arcs = 0

        board = self.sudoku.board

        # Iterate over each row and column
        for row in range(len(board)):
            for col in range(len(board[row])):

                # Only add arcs that originate from Fields that are not finalized
                # Arcs from fields that are finalized do nothing and increase complexity
                if not board[row][col].is_finalized():
                    # Get the neighbors of this field
                    for neighbor in board[row][col].get_neighbours():
                        # Create a tuple of the current Field and a neighbor and store in queue
                        num_arcs += 1

                        if self.heuristic is None:
                            new_arc = Arc(board[row][col], neighbor)
                        else:
                            new_arc = self.heuristic(board[row][col], neighbor)

                        self.priority_queue.put(new_arc)

        print("Number of arcs loaded: " + str(num_arcs))

    def valid_solution(self):
        """
        Checks the validity of a sudoku solution
        @return: true if the sudoku solution is correct
        """
        board = self.sudoku.board

        # Iterate over each row and column
        for row in range(len(board)):
            for col in range(len(board[row])):

                if board[row][col].get_value() == 0:
                    return False

                for neighbor in board[row][col].get_neighbours():
                    if board[row][col].get_value() == neighbor.get_value():
                        return False

        return True
