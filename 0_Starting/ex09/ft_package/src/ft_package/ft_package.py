def count_in_list(lst: list[str], search: str) -> int:
    """Returns an int of how many times 'search'
    appears in 'lst'"""
    return lst.count(search)


def morse_translate(string) -> str:
    """takes a string and translates it into morse code"""

    NESTED_MORSE = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        " ": "/",
        "\n": "\n",
    }
    morse_code = []
    for c in string.upper():
        if c in NESTED_MORSE:
            morse_code.append(NESTED_MORSE[c])
        else:
            raise AssertionError(f"can't convert char '{c}'.")
    return " ".join(morse_code)


def banana_size(nbr: int) -> str:
    """Converts given int to banana scale
    (1 banana == 7 inches)"""
    return f"{nbr / 7:.2f} bananas"


def duck_translate(text: str) -> str:
    """Translates given text to language a duck could understand."""
    return " quack ".join(text.split())
