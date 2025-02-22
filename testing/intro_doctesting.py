
"""
Explanation of Doctests:

Doctests are a simple way to check that your code behaves as expected by embedding test cases inside your docstrings.
Here’s how they work:

Inside a function's docstring, you write examples of how the function should behave using Python’s interactive shell syntax.
    - The example starts with `>>>` followed by a function call.
    - The expected result comes on the next line without `>>>`.

You can run doctests using Python's built-in `doctest` module. By using the command:
    python -m doctest my_script.py -v
This will execute all doctests in the script and verify that the function’s output matches the expected output in the docstrings.

What happens if the tests fail?
    - If the function’s output does **not** match the expected output in the docstring, the test will fail.
    - `doctest` will show you the actual output and highlight the discrepancy.
    - You can then adjust your function or update your docstring accordingly.

Why use doctests?
    - **Quick validation**: It’s a great way to quickly check if your functions are working as expected.
    - **Documentation**: Doctests double as both documentation (by showing usage examples) and tests.
    - **Lightweight**: They’re simple to add and don't require setting up test suites.
"""


def add(a, b):
    """
    Adds two numbers together and returns the result.

    This function takes two arguments and returns their sum. It also works for negative numbers and zero.

    Example usage:

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    >>> add(100, -50)
    50
    >>> add(0, -10)
    -10

    The function handles both integers and floating-point numbers:

    >>> add(3.5, 2.5)
    6.0
    >>> add(1.1, 2.2)
    3.3

    Args:
        a (int, float): The first number to be added.
        b (int, float): The second number to be added.

    Returns:
        int, float: The sum of the two numbers.
    """
    return a + b


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# To run doctests manually, use the following command in your terminal:
# python -m doctest my_script.py -v
