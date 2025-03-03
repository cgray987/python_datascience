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
    try:
        ac = len(sys.argv)

        if ac > 2:
            raise AssertionError("Too many arguments for this puny program")
        if ac == 1:
            try:
                print("What is the text to count?")
                s = ""
                # this is silly, but in order to handle both EOF and \n.
                # input would be much simpler.
                while True:
                    char = sys.stdin.read(1)
                    s += char
                    if not char or char == "\n":
                        break
            except EOFError:
                pass
        else:
            s = sys.argv[1]
        word_count(s)
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")


if __name__ == "__main__":
    main()
