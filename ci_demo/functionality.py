import numbers


def greet():
    return 'Hello'


def minimum(*args):

    if not any([isinstance(arg, numbers.Real) for arg in args]):
        return

    the_min = float("inf")
    for arg in args:
        if isinstance(arg, numbers.Real):
            the_min = min(the_min, arg)

    return the_min
