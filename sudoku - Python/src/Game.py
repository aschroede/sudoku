from collections import deque


class Game:

    def __init__(self, sudoku):
        self.sudoku = sudoku

    def show_sudoku(self):
        print(self.sudoku)

    def solve(self):
        """
        Implementation of the AC-3 algorithm
        @return: true if the constraints can be satisfied, false otherwise
        """
        queue = self.load_arcs()

        while queue:

            arc = queue.popleft()
            m = arc[0]
            n = arc[1]

            if not m.is_finalized():

                domain_changed = self.revise(arc)

                if m.get_domain_size() == 0 and m.get_value() == 0:
                    return False

                if domain_changed:

                    for neighbor in m.get_other_neighbours(n):

                        new_arc = (neighbor, m)

                        if new_arc not in queue:
                            queue.append(new_arc)

        return True

    @staticmethod
    def revise(arc):

        m = arc[0]
        n = arc[1]

        domain_changed = False

        # Only restrict domain if value of neighbor is finalized
        if n.is_finalized():
            for value in m.get_domain():
                if value == n.get_value():
                    domain_changed = True
                    m.remove_from_domain(value)

        return domain_changed

    def load_arcs(self):

        queue = deque()
        board = self.sudoku.board

        # Iterate over each row and column
        for row in range(len(board)):
            for col in range(len(board[row])):

                # Get the neighbors of this field
                for neighbor in board[row][col].get_neighbours():
                    # Create a tuple of the current Field and a neighbor and store in queue
                    queue.append((board[row][col], neighbor))

        return queue

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
