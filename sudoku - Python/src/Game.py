from queue import PriorityQueue


class Game:

    def __init__(self, sudoku, heuristic):
        self.sudoku = sudoku
        self.heuristic = heuristic
        self.priority_queue = PriorityQueue()

        # Counters for statistics
        self.complexity = 0
        self.num_initial_arcs_loaded = 0
        self.num_revised_arcs_loaded = 0
        self.revisions = 0

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

            # Only process arc (A, B) if A is not finalized. Wasted effort otherwise.
            if not arc.a.is_finalized():

                # Revise arc
                domain_changed = self.revise(arc)

                # If A has a domain size of 0 and has not been assigned a number from 1-9
                # then this field is not solvable and thus the sudoku is not solvable
                if arc.a.get_domain_size() == 0 and arc.a.get_value() == 0:
                    return False

                if domain_changed:
                    for neighbor in arc.a.get_other_neighbours(arc.b):

                        # Only create a new arc if neighbor is not finalized. Wasted effort otherwise.
                        if not neighbor.is_finalized():
                            new_arc = self.heuristic(neighbor, arc.a)

                            # Only add new arc if not in queue already.
                            if new_arc not in self.priority_queue.queue:
                                self.num_revised_arcs_loaded += 1
                                self.priority_queue.put(new_arc)

        return True

    def revise(self, arc):
        """

        @param arc: Arc (A, B) to revise is composed of the two fields A and B. Field A's domain is revised
        if B is finalized. A's domain is revised by removing the finalized value of B from A's domain if it exists.
        @return: True if A's domain has been revised, otherwise false.
        """
        domain_changed = False

        # Only restrict domain of A if B is finalized in arc (A, B)
        if arc.b.is_finalized():

            # Test each value in A's domain
            for value in arc.a.get_domain():

                # If there is a matching value in B's domain, remove that value from A's domain
                if value == arc.b.get_value():
                    self.revisions += 1
                    domain_changed = True
                    arc.a.remove_from_domain(value)

        return domain_changed

    def load_arcs(self):
        """
        Create all constraints (arcs) and load them into the queue.
        """
        board = self.sudoku.board

        # Iterate over each row and column
        for row in range(len(board)):
            for col in range(len(board[row])):

                # Only add arcs that originate from Fields that are not finalized
                # Arcs from fields that are finalized do nothing and increase complexity
                if not board[row][col].is_finalized():

                    # Get the neighbors of this field
                    for neighbor in board[row][col].get_neighbours():
                        self.num_initial_arcs_loaded += 1

                        # Create a tuple of the current Field and a neighbor and store in queue
                        new_arc = self.heuristic(board[row][col], neighbor)

                        # Add to queue
                        self.priority_queue.put(new_arc)

    def valid_solution(self):
        """
        Checks the validity of a sudoku solution
        @return: true if the sudoku solution is correct
        """
        board = self.sudoku.board

        # Iterate over each row and column
        for row in range(len(board)):
            for col in range(len(board[row])):

                # If a field has not been set to a number in range 1-9 the sudoku is not solved
                if board[row][col].get_value() == 0:
                    return False

                # if a field has a value that is the same as any of it's 20 neighbors then a constraint
                # has been violated and the sudoku is not solved.
                for neighbor in board[row][col].get_neighbours():
                    if board[row][col].get_value() == neighbor.get_value():
                        return False

        return True
