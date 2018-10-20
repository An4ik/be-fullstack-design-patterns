class OperationalNumber(object):
    """
    Used for basic math operations
    """

    def __init__(self, value):
        """
        Constructor of the class, interpretator called when you create an instance

        :param value : value  of the Object.
        :param type value :int

        if value is not number than returns error
        """
        if type(value) not in [int, float]:
            raise TypeError("Value must be real number.")
        self.value = value

    def __add__(self, other):
        """
        Addition of two numbers
        """
        return self.value + other.value

    def __sub__(self, other):
        """
        Subtraction of two numbers
        """
        if other.value > self.value:
            raise ValueError("Second value is bigger than first value")
        return self.value - other.value

    def __mul__(self, other):
        """
        Multiplication of two numbers
        """
        return self.value * other.value

    def __truediv__(self, other):
        """
        Division of two numbers
        """
        if other.value == 0:
            raise ValueError("Zero division error.")
        return self.value / other.value

    def __mod__(self, other):
        """
        Mod of division
        """
        if other.value == 0:
            raise ValueError("Zero division error.")
        return self.value % other.value

    def __eq__(self, other):
        """
        Compares two numbers for equality
        """
        return self.value == other.value

    def __gt__(self, other):
        """
        Greater than operator (self.value > other.value)
        """
        return self.value > other.value

    def __lt__(self, other):
        """
        Less than operator (self.value < other.value)
        """
        return self.value < other.value
