from S1E9 import Character


class Baratheon(Character):
    """Baratheon character class"""
    def __init__(self, first_name, is_alive=True):
        """Init Baratheon character with first name"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hair = "dark"

    def die(self):
        """💀 kill Baratheon"""
        self.is_alive = False

    def __str__(self):
        """str method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def __repr__(self):
        """returns printable representation of object (str)"""
        return self.__str__()


class Lannister(Character):
    """Lannister character class"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hair = "light"

    def die(self):
        """💀 kill Lannister"""
        self.is_alive = False

    def __str__(self):
        """str method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def __repr__(self):
        """returns printable representation of object (str)"""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Creates lannister characters in a chain
        cls -> refers to class itself w/o creating instance
        first_name -> str
        is_alive -> bool"""
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance
