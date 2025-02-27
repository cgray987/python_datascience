def all_thing_is_obj(object: any) -> int:
    t = type(object)
    accepted_types = {list, tuple, set, dict}

    if isinstance(object, str):
        print(object, "is in the kitchen", ":", t)
    elif t in accepted_types:
        print(t.__name__.capitalize(), ":", t)
    else:
        print("Type not found")
    return 42
