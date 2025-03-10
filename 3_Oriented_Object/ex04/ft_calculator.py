class calculator:
    """A simple vector calculator. Calculates and prints
    new vector. Uses static methods as to not
    instantiate the class itself. Both vectors provided
    must be the same length. No error checking.

    Accepts:
        V1 (list(float))
        V2 (list(float))
    Static Methods:
        dotproduct
        add_vec
        sub_vec
        """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Prints dot-product of the given vectors
        a•b = sum_n(a_n*b_n)"""
        dot = 0.0
        for i in V1:
            dot += i * V2[V1.index(i)]
        print(f"Dot product\t: {int(dot)}")

    @staticmethod
    def add_vector(V1: list[float], V2: list[float]) -> None:
        """Prints result of adding two given vectors"""
        res = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add vector\t: {res}")

    @staticmethod
    def sub_vector(V1: list[float], V2: list[float]) -> None:
        """Prints result of subtracting two given vectors"""
        res = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sub vector\t: {res}")
