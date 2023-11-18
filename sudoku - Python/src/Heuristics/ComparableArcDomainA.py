import functools
from src.Arc import Arc

"""Comparable class that wraps arcs and sorts them based on the domain size of Field A in arc (A, B)"""


@functools.total_ordering
class ComparableArcDomainA(Arc):

    def __lt__(self, other):
        return self.a.get_domain_size() < other.a.get_domain_size()

    def __gt__(self, other):
        return self.a.get_domain_size() > other.a.get_domain_size()
