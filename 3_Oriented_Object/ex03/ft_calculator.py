class calculator:
    """A simple calculator with addition, subtraction
    multiplication and division of a
    vector with a scalar.

    Accepts:
        vector (list): the list of numbers on
                        which operations will be applied to

    Methods:
        __init__(self, vector)
        __add__(self, object): +
        __mul__(self, object): *
        __sub__(self, object): -
        __truediv__(self, object): /"""

    def __init__(self, vector):
        """inits the calculator with provided list"""
        self.vector = vector

    def __add__(self, obj):
        """addition"""
        self.vector = [x + obj for x in self.vector]
        print(self.vector)
        return self.vector

    def __mul__(self, obj):
        """multiplication"""
        self.vector = [x * obj for x in self.vector]
        print(self.vector)
        return self.vector

    def __sub__(self, obj):
        """subtraction"""
        self.vector = [x - obj for x in self.vector]
        print(self.vector)
        return self.vector

    def __truediv__(self, obj):
        """division (raises ZeroDivisinError if obj == 0)"""
        try:
            if obj == 0:
                raise ZeroDivisionError("divide by zero")
            self.vector = [x / obj for x in self.vector]
            print(self.vector)
            return self.vector
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError: {e}")
