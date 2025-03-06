import numpy as np


def slice_me(family: list,
             start: int,
             end: int) -> list:
    """
    Prints shape of family list,
    returns sliced array from start->end
    """
    try:
        if not isinstance(family, list) \
            or not isinstance(start, int) \
                or not isinstance(end, int):
            raise TypeError(
                "Wrong types for function")
        if not all(len(x) == len(family[0]) for x in family):
            raise ValueError(
                "List sizes not consistant")

        print(f"my shape is : {np.shape(family)}")
        r = np.array(family)[start:end]
        print(f"my new shape is : {r.shape}")
        return r.tolist()
    except Exception as e:
        print(f"Exception: {e}")
