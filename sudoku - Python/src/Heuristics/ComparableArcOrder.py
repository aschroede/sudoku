import functools
from src.Arc import Arc
from itertools import count


@functools.total_ordering
class ComparableArcOrder(Arc):
    counter = count()

    def __init__(self, m, n):
        # Call the constructor of the parent class
        super().__init__(m, n)

        # Initialize parameters specific to the child class
        self.priority = next(ComparableArcOrder.counter)
        # Other initialization code for the child class

    # def __eq__(self, other):
    #     return (self.m, self.n, self.priority) == (other.m, other.n, other.priority)

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority
