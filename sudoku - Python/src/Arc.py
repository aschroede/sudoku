class Arc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        """
        Function for determining the equality of two arcs

        @param other: arc to compare two
        @return: true/false depending on if the arcs are equal
        """
        return (self.a, self.b) == (other.a, other.b)
