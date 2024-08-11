import sys


def main():
    """
    main function which counts appereance of
    "upper letters", "lower letters", "punctuation marks",
    "spaces", "digits"
    of first given argv
    """
    try:
        sys.argv[2]
        print("AssertionError")
        return
    except Exception:
        pass
    try:
        string = sys.argv[1]
    except Exception:
        string = "Hello World!"
        print("What is the text to count?")
        string = input()
    # print(len(string))
    list_strs = ["upper letters", "lower letters", "punctuation marks"]
    list_strs.append("spaces")
    list_strs.append("digits")
    list_count = [0, 0, 0, 0, 0, 0]
    punctuation = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~\"\\"
    punctuation += '"'
    punctuation += "\\"
    for e in string:
        if e.isupper():
            list_count[0] += 1
        elif e.islower():
            list_count[1] += 1
        elif e in punctuation:
            list_count[2] += 1
        elif e.isspace():
            list_count[3] += 1
        elif e.isnumeric():
            list_count[4] += 1
        list_count[5] += 1
    print("The text contains", list_count[5],  "characters:")
    for i in range(5):
        print(list_count[i], list_strs[i])


if __name__ == "__main__":
    main()
