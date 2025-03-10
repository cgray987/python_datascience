import random
import string
from dataclasses import dataclass, field

"""
dataclass:
    provides decorator and functions for automatically adding
    generated special methods to user-defined classes.
dataclass.field():
    Adds functionality to dataclass per-field information
        init: if true, field is included as a parameter to __init__ method
        default: if true, that field will be a default value
dataclass.__post_init__():
    When defined, it will be called by generated __init__. Used for
    initializing fileds dependant on other fields.
"""


def generate_id() -> str:
    """Generates random lowercase ascii string 15 chars long."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class.

    Attributes:
        name (str): first name
        surname (str): last name
        active (bool): default True -- student's current status
        login (str): login str generated from name/surname
        id (str): unique identifier for student, generated by
                    generate_id()

    Methods:
        __post_init__(self): generates students login"""

    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """post_init method to create login based on name/surname"""
        self.login = self.name[0].capitalize() + self.surname.lower()
