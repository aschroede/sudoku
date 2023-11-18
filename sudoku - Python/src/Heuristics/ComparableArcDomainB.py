import functools
from src.Arc import Arc


"""Comparable class that wraps arcs and sorts them based on the domain size of Field B in arc (A, B)"""


@functools.total_ordering
class ComparableArcDomainB(Arc):

    def __lt__(self, other):
        return self.b.get_domain_size() < other.b.get_domain_size()

    def __gt__(self, other):
        return self.b.get_domain_size() > other.b.get_domain_size()
