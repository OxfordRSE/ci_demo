import numbers


def greet(name=""):
    """
    A function that takes a name and returns a greeting.

    Parameters
    ----------
    name : str, optional
        The name to greet (default is "")

    Returns
    -------
    str
        The greeting
    """
    return "Hello " + name


def minimum(*args):
    """
    A function taking some arguments and returning the minimum number among the arguments.

    Parameters
    ----------
    args : int, float
        The numbers from which to return the minimum

    Returns
    -------
    int,float
        The minimum
    """
    if not any([isinstance(arg, numbers.Real) for arg in args]):
        return

    the_min = float("inf")
    for arg in args:
        if isinstance(arg, numbers.Real):
            the_min = min(the_min, arg)

    return the_min
