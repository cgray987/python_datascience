from ft_filter import ft_filter


class c:
    RED = "\033[0;31m"
    GRN = "\033[0;32m"
    CYN = "\033[0;36m"
    RST = "\033[0m"


def print_ok_ko(test, mine, expected):
    """prints test results"""
    print(f"{c.CYN}~~~~Test: {test}~~~~{c.RST}")
    print(mine)
    print(expected)
    if mine == expected:
        print(c.GRN + "~~~~\tOK\t~~~~" + c.RST)
    else:
        print(c.RED + "~~~~\tKO\t~~~~" + c.RST)


def main():
    """tests ft_filter against filter"""
    list1 = [1, 2, 3, 4, 5, 6]

    def lambda1(x):
        lambda x: x % 2 == 0

    test1 = list(ft_filter(lambda1(list1), list1))
    expected1 = list(filter(lambda1(list1), list1))
    print_ok_ko("even number list", test1, expected1)

    list2 = [
        "array of strings",
        1,
        42.42,
        "YELLING",
        "somewHAT YELLIng",
        "dig1235",
        "DIG12345",
    ]

    def lower(string):
        if isinstance(string, str):
            return string.islower()

    test2 = list(ft_filter(lower(list2), list2))
    expected2 = list(filter(lower(list2), list2))
    print_ok_ko("lower filter", test2, expected2)

    list3 = ["mix types", 1, 0, None, "1", 42.42, [1, 2],
             "test", 999999999999999]

    def lambda3(x):
        lambda x: isinstance(x, int)

    test3 = list(ft_filter(lambda3(list3), list3))
    expected3 = list(filter(lambda3(list3), list3))
    print_ok_ko("mixed types", test3, expected3)


if __name__ == "__main__":
    main()
