import functools
from Arc import Arc


@functools.total_ordering
class ComparableArcFinalized(Arc):

    def __lt__(self, other):
        return self.n.is_finalized() > other.n.is_finalized()

    def __gt__(self, other):
        return self.n.is_finalized() < other.n.is_finalized()