from abc import ABC, abstractmethod


class Character(ABC):
    """Generic character constructor"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """takes a first_name as a string and optionally
        is_alive bool. Defaults to True."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """implemented in subclasses"""
        pass


class Stark(Character):
    """Class for Stark character (i guess game of thrones shit?)"""
    def __init__(self, first_name, is_alive=True):
        """Creating Stark character"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """💀"""
        self.is_alive = False
