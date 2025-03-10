from typing import Any


def callLimit(limit: int):
    """Takes an int 'limit' that restricts execution
    'limit' number of times. If function is called more
    than 'limit' number of times, raise AssertionError

    Parameters:
        limit(int): Number of times the function can be called
    Returns:
        function: Decorator function that restricts number of times
        a function can be called."""
    count = 0

    def callLimiter(function):
        """Decorator function:
            Wraps around limit_function, counting number of times
            the target function is called."""

        def limit_function(*args: Any, **kwds: Any):
            """Wrapper function:
                Increments count variable, if still under limit,
                execute function. Otherwise, raise AssertionError"""
            try:
                nonlocal count
                count += 1
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} called too many times.")
            except AssertionError as e:
                print(f"Error: {e}")

        return limit_function

    return callLimiter
