

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


def my_len(string):
    """gets len of argument"""
    counter = 0
    for e in string:
        counter += 1
    return counter


def ft_tqdm(iterable):
    """basic implementation of ft_tqdm"""
    total = my_len(iterable)

    def print_progress(iteration):
        """printing current state"""
        progress = iteration / total
        width = 60
        blocks = my_to_int("%.0f" % ((progress * width) // 1))
        # print(blocks)
        progress *= 100
        progress = "%.0f" % progress
        if progress != "100":
            progress = " " + progress
        if blocks > 0:
            bar = f"\r{progress}%|[{(blocks - 1) * "="}>{(width - blocks) * " "}]| {iteration}/{total}"
        else:
            bar = f"\r{progress}%|[>{(width - blocks) * " "}]| {iteration}/{total}"
        print(bar, flush=True, end="")

    for i, item in enumerate(iterable):
        yield item
        print_progress(i + 1)