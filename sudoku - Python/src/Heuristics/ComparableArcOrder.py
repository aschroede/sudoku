import functools
from itertools import count
from src.Arc import Arc

"""
Comparable class that wraps arcs and sorts them based on the priority passed to the constructor. The 
priority is the order in which the arcs are created and is assigned via the static counter in this class.
"""


@functools.total_ordering
class ComparableArcOrder(Arc):
    counter = count()

    def __init__(self, m, n):
        super().__init__(m, n)
        self.priority = next(ComparableArcOrder.counter)

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority
