import sys


def main():
    try:
        sys.argv[2]
        print("AssertionError: more than one argument is provided")
    except Exception:
        try:
            t = sys.argv[1]
            seen = False
            last = ""
            for e in t:
                if (e == "+" or e == "-") and not seen:
                    seen = 1
                elif (e == "+" or e == "-") and seen:
                    print("AssertionError: argument is not an integer")
                    return
                elif not e.isnumeric():
                    print("AssertionError: argument is not an integer")
                    return
                last = e
            if not last.isnumeric():
                print("AssertionError: argument is not an integer")
                return
            even = ["2", "4", "6", "8", "0"]
            if last in even:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except Exception:
            return

if __name__ == "__main__":
    main()