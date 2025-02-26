import sys


def word_count(s: str) -> int:
    """returns character counts for given string"""

    characters = len(s)
    punctuation = "!”#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    punc = sum(1 for c in s if c in punctuation)
    spaces = sum(1 for c in s if c.isspace())
    digits = sum(1 for c in s if c.isdigit())

    print(f"The text contains {characters} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    ac = len(sys.argv)

    assert ac <= 2, "Too many arguments for this puny program"
    if ac == 1:
        s = input("Give me a string: ")
    else:
        s = sys.argv[1]
    word_count(s)


if __name__ == "__main__":
    main()
