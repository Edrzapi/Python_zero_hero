# Decorators can seem confusing, lets break the concept down with useful functions
# In Python, decorators are a powerful and flexible way to modify or extend the behavior of functions or methods without
# changing their actual code. They are often used to add functionality, such as logging, access control, memoization
# , or modifying how a function behaves.


# Logging Time

import time  # Import time module to measure execution time


def func_time(func):  # Decorator function that takes another function as an argument
    def wrapper():  # Inner function that wraps the original function
        pre_execution_stamp = time.time()  # Capture time before function execution
        func()  # Call the original function
        post_execution_stamp = time.time() - pre_execution_stamp  # Measure elapsed time
        print(f"{func.__name__} executed in: {post_execution_stamp:.4f} seconds")  # Log the execution time

    return wrapper  # Return the wrapper function without executing it


@func_time  # Apply the decorator to measure execution time
def sleep_for_three():
    time.sleep(3)  # Simulate a function that takes 3 seconds to execute


sleep_for_three()  # Call the function, which is now wrapped

# Argument Logging

import functools  # Required for preserving function metadata


def log_function_call(func):
    """Decorator to log function calls, arguments, and return values."""

    @functools.wraps(func)  # Preserve the original function name and docstring
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with arguments: {args} {kwargs}")
        result = func(*args, **kwargs)  # Call the original function
        print(f"{func.__name__} returned: {result}")  # Log the result
        return result  # Return the original function's output

    return wrapper  # Return the wrapper function


@log_function_call
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


# Example usage
sum_result = add(3, 5)
