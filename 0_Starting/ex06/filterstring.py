import sys
import ft_filter


def main():
    try:
        ac = len(sys.argv)
        if (ac != 3):
            raise AssertionError("the arguments are bad")
        S = sys.argv[1]
        N = int(sys.argv[2])
        if N is None:
            raise AssertionError("the arguments are bad")
        if S.find("!”#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"):
            raise AssertionError("the arguments are bad")
		if not isinstance(S, N) or not isinstance(N, int):
			raise AssertionError("the arguments are bad")
        
		tab = S.split(" ")
        filtered = ft_filter(lambda word: len(word) > N, tab)
        for x in filtered:
            print(x)
        

    except AssertionError as e:
        print(f"AssertionError: {str(e)}")


if __name__ == "__main__":
    main()
