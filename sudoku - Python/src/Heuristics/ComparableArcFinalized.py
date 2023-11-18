import functools
from src.Arc import Arc


@functools.total_ordering
class ComparableArcFinalized(Arc):

    # We want finalized fields to come first
    def __lt__(self, other):
        return self.b.is_finalized() > other.b.is_finalized()

    def __gt__(self, other):
        return self.b.is_finalized() < other.b.is_finalized()