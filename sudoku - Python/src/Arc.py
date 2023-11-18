class Arc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        return (self.a, self.b) == (other.a, other.b)
