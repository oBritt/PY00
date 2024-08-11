from ft_filter import ft_filter
import sys


def my_len(string):
    """gets len of argument"""
    counter = 0
    for e in string:
        counter += 1
    return counter


def my_to_int(str: str):
    """conerts a string to int"""
    values = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0,
    }
    number = 0
    for e in str:
        number = number * 10 + values[e]
    return number


def print_valid(strings: str, length: str):
    """function which checks if args are OK
       and prints only long enough words"""
    if not length.isdigit():
        return 1
    wordss = strings.split(' ')
    words = [word.lstrip() for word in wordss]
    for word in words:
        if not word:
            continue
        if not word.isalnum():
            return 1
    print(ft_filter(lambda x: my_len(x) > my_to_int(length), words))
    return 0


def main():
    """main function does the whole job"""
    try:
        sys.argv[1]
        sys.argv[2]
        try:
            sys.argv[3]
            print("AssertionError: the amount of arguments is not 2")
            return
        except Exception:
            pass
        if print_valid(sys.argv[1], sys.argv[2]):
            print("AssertionError: the arguments are bad")
    except Exception:
        print("AssertionError: the amount of arguments is not 2")
        return


if __name__ == "__main__":
    main()

# print(my_to_int.__doc__)
