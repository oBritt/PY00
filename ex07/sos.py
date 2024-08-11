import sys


def my_len(string):
    """gets len of argument"""
    counter = 0
    for e in string:
        counter += 1
    return counter


def main():
    """main function of programm checks args and makes it work"""
    if (my_len(sys.argv) != 2):
        print("AssertionError: the amount of arguments is bad")
        return
    if not sys.argv[1].isalnum():
        print("AssertionError: the arguments are bad")
        return
    string = sys.argv[1]
    NESTED_MORSE = {
        " ": "/",
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..",
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
        "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
        "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
        "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
        "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
        "y": "-.--", "z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
    }
    first = 1
    for e in string:
        if not first:
            print(" ", end="")
        first = 0
        print(NESTED_MORSE[e], end="")


if __name__ == "__main__":
    main()
