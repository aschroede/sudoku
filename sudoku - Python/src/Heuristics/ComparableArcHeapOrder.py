import functools

from src.Arc import Arc


@functools.total_ordering
class ComparableArcHeapOrder(Arc):

    def __init__(self, m, n):
        super().__init__(m, n)

        # By setting the priority of all items to one the underlying heap structure determines the order.
        self.priority = 1

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority
