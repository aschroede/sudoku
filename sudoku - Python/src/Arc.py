class Arc:

    def __init__(self, m, n):
        self.m = m
        self.n = n

    def __eq__(self, other):

        if isinstance(other, tuple):
            return (self.m, self.n) == (other[1].m, other[1].n)
        else:
            return (self.m, self.n) == (other.m, other.n)

    def __ne__(self, other):
        return not (self == other)
