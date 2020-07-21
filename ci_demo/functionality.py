import numbers


def greet(name=""):
    """
    A function that takes a name and returns a greeting.

    :param name: the name to greet, default to ""
    :type name: str
    :return: the greeting
    :rtype: str
    """
    return "Hello " + name


def minimum(*args):
    """
    A function taking some arguments and returning the minimum number among the arguments.

    :param args: numbers from which to return the minimum
    :type args: int,float
    :return: the minimum
    :rtype: int,float
    """
    if not any([isinstance(arg, numbers.Real) for arg in args]):
        return

    the_min = float("inf")
    for arg in args:
        if isinstance(arg, numbers.Real):
            the_min = min(the_min, arg)

    return the_min
