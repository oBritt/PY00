

def all_thing_is_obj(object: any) -> int:
    t = ["list", "tuple", "dict", "set"]
    type_of = object.__class__.__name__
    if (type_of in t):
        print(object.__class__.__name__.capitalize(), ":", object.__class__)
    elif type_of == "str":
        print(object, "is in the kitchen", ":", object.__class__)
    else:
        print("Type not found")
    return 42