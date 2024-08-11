

def ft_filter(func, args):
    """
        copy of filter function does the same as filter
        ft_filter(function or None, iterable) --> filter object
        Return an iterator yielding those items of
        iterable for which function(item)
        is true. If function is None, return the items that are true.
    """
    if func:
        return [e for e in args if func(e)]
    else:
        return [e for e in args if e]
