from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class inherits from both Baratheon and Lannister"""

    def __init__(self, first_name, is_alive=True):
        """init King"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """set eye color"""
        self.eyes = color

    def get_eyes(self):
        """get eye color"""
        return self.eyes

    def set_hair(self, color):
        """set hair color"""
        self.hair = color

    def get_hair(self):
        """get hair color"""
        return self.hair
