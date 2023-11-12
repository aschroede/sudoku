class Field:

    # region constructor

    def __init__(self, *args):

        self.domain = []
        self.value = 0
        self.neighbours = []

        # Constructor in case the field is unknown
        if len(args) == 0:
            for i in range(1, 10):
                self.domain.append(i)

        # Constructor in case the field is known, i.e., it contains a value
        if len(args) == 1:
            self.value = args[0]
            self.domain = []

    # endregion

    # region value functions

    def is_finalized(self):
        return self.value != 0

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    # endregion

    # region neighbor functions

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours

    def get_neighbours(self):
        return self.neighbours

    def get_other_neighbours(self, b):
        new_neighbours = self.neighbours
        new_neighbours.remove(b)
        return new_neighbours

    # endregion

    # region domain functions

    def get_domain(self):
        return self.domain

    def get_domain_size(self):
        """

        @return:
        """
        return len(self.domain)

    def remove_from_domain(self, value):
        """
        Removes the given value from the domain, and possibly assigns the last value to the field

        :param value: value to remove
        :return: true if the value was removed
        """
        b = self.domain.remove(value)

        if len(self.domain) == 1:
            self.set_value(self.domain[0])

        return b

    # endregion

    # region Misc Functions

    def __str__(self):
        return "." if self.value == 0 else str(self.value)

    # endregion
