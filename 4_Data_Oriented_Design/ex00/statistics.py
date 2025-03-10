from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculates and prints various statistics from 'args'

    Parameters:
        *args: Variable number of positional args
                -> the values for caluclations
        **kwargs: Keyword args to determine what stats to print
                ->mean, median, quartile, std_dev, and variance
    """
    args_list = list(args)
    args_list.sort()
    total = sum(args_list)
    num_args = len(args_list)

    if num_args == 0:
        for value in kwargs.items():
            print("ERROR")
        return

    mean = total / num_args
    median_index = num_args // 2
    if num_args % 2 == 0:
        median = (args_list[median_index - 1]
                  + args_list[median_index]) / 2
    else:
        median = args_list[median_index]

    q1_index = num_args // 4
    q3_index = q1_index * 3
    quartile = [float(args_list[q1_index]),
                float(args_list[q3_index])]

    variance_total = 0
    for x in args_list:
        variance_total += (x - mean) ** 2
    variance = variance_total / num_args
    std_dev = (variance ** 0.5)

    res = {"mean": mean, "median": median, "quartile": quartile,
           "std": std_dev, "var": variance}
    for _, value in kwargs.items():
        if value in res:
            print(f"{value} : {res[value]}")
