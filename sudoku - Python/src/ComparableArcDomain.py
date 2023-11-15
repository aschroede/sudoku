import functools
from Arc import Arc


@functools.total_ordering
class ComparableArcDomain(Arc):

    def __lt__(self, other):
        return self.m.get_domain_size() < other.m.get_domain_size()

    def __gt__(self, other):
        return self.m.get_domain_size() > other.m.get_domain_size()