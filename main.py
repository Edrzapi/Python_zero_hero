print("Hello World")


def add(a, b):
    """
    Adds two numbers together.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    return a + b


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# python -m doctest my_script.py -v
