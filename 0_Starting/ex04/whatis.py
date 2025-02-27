import sys


def main():
    ac = len(sys.argv)
    if ac == 1:
        return
    if ac > 2:
        raise AssertionError("more than one argument is provided")
    try:
        num = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if num % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")
