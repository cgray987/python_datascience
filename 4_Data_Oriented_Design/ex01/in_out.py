def square(x: int | float) -> int | float:
    """Returns the square (x^2) of the provided argument."""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns the argument to its own power"""
    return x ** x


def outer(x: int | float, function) -> object:
    """Takes a number and a function; returns a callable
    object that acts as its counter.

    Each time the counter function is called, calculate the resultant
    applied to its input number, update the original input, and return
    the result."""
    def inner() -> float:
        """execute provided function, update, and return result

        use nonlocal variable to pass variables from parent's scope"""
        nonlocal x
        result = function(x)
        x = result
        return result
    return inner
