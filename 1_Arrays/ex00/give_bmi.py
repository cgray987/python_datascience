def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Returns BMI (body-mass index) from given list of heights/weights"""
    if len(height) != len(weight):
        raise ValueError("lists of height and weights must be same size")
    bmi_list = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError(
                "lists of height and weights must be int or floats"
                )
        if h <= 0 or w <= 0:
            raise ValueError("Height and weight must be > 0")
        bmi_list.append(w / (h**2))
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Returns true for each given bmi over given limit """
    if not isinstance(limit, (int, float)):
        raise TypeError("limit must be int or float")
    over_limit = []
    for x in bmi:
        if not isinstance(x, (int, float)):
            raise TypeError("BMI must be int or float")
        over_limit.append(x > limit)
    return over_limit
