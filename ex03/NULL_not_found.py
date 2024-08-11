def is_nan(value):
    return value != value

def NULL_not_found(object: any) -> int:
    # print(f'{object=}'.split('=')[0])
    d = {None: "Nothing:",
         0: "Zero:",
         "": "Empty:",
         False: "Fake:"}
    
    try:
        if is_nan(object):
            print("Cheese:", object, object.__class__)
        else:
            print(d[object], object, object.__class__)
    except Exception:
        print("Type not Found")
        return 1
    return 0