import sys
from ft_filter import ft_filter


def main():
    """Takes two args, String S and int N

    Splits string into words by spaces and filters
    those that are shorter than N"""
    try:
        ac = len(sys.argv)
        if ac != 3:
            raise AssertionError("the arguments are bad")
        input_str = sys.argv[1]
        try:
            min_word_len = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        if not isinstance(input_str, str) or not isinstance(min_word_len, int):
            raise AssertionError("the arguments are bad")
        if input_str.find("!”#$%&'()*+,-./:;<=>?@[\\]^_`{|}~") != -1:
            raise AssertionError("the arguments are bad")

        def L(word): lambda word: len(word) > min_word_len
        filtered = list(ft_filter(L, input_str.split(" ")))
        print(filtered)

    except AssertionError or ValueError as e:
        print(f"AssertionError: {str(e)}")


if __name__ == "__main__":
    main()
