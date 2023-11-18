import functools
from src.Arc import Arc


"""Comparable class that wraps arcs and sorts them based on if Field B is finalized in arc (A, B)"""


@functools.total_ordering
class ComparableArcFinalized(Arc):

    # We want finalized fields to come first
    def __lt__(self, other):
        return self.b.is_finalized() > other.b.is_finalized()

    def __gt__(self, other):
        return self.b.is_finalized() < other.b.is_finalized()