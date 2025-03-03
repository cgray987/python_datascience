def NULL_not_found(object: any) -> int:
    t = type(object)

    if object is None:
        print("Nothing:", object, t)
    elif t is float:
        print("Cheese:", object, t)
    elif t is int:
        print("Zero:", object, t)
    elif t is bool:
        print("Fake:", object, t)
    elif t is str and not object:
        print("Empty:", object, t)
    else:
        print("Type not found")
        return 1
    return 0
