# Python Functions: A Practical Guide

# Basic Function Definition
# A function either performs a task or returns a value.

def new_function(para, para_one):
    result = para + para_one
    return result


# Default Arguments
# When you provide default values for parameters, the caller can omit those arguments.

def next_function(no, first_name="bob", last_name="jones"):
    return "{0}, {1}, {2}".format(no, first_name, last_name)


print(next_function(1))  # Uses default names
print(next_function(1, first_name="Ed"))  # Pass by name


# You cannot pass positional arguments after keyword arguments

# 3. Variadic Functions (Variable-Length Arguments)
# Functions that accept a variable number of arguments.
# *args: For a variable number of positional arguments
# **kwargs: For a variable number of keyword arguments

# Example using *args (variable-length positional arguments) here 3-6 will be represented as a tuple
def variadic_function(a, b, *z):
    return a, b, z


print(variadic_function(1, 2, 3, 4, 5, 6))


# Example using **kwargs (variable-length keyword arguments)
# here the output will be 'vatpc': 15, 'gross': 9.55, 'message': 'Summary'
def print_vat(**kwargs):
    print(kwargs)


print_vat(vatpc=15, gross=9.55, message='Summary')


# Keyword-Only Arguments
# Using * enforces keyword-only arguments.

def force_function(*, no=0, first_name="bob", last_name="jones"):
    return "{0}, {1}, {2}".format(no, first_name, last_name)


# Unpacking Arguments
# You can unpack tuples or lists into function arguments.

def unpack_function(a, b, c):
    return a, b, c


new_tup = "One", "Two", "Three"
unpack_function(*new_tup)


# Nested Functions
# Functions can be defined inside other functions.

def outer_func():
    print("Outer function!")

    def inner_func():
        print("Inner function!")

    inner_func()


outer_func()


# Using Functions to Return Other Functions (Nesting Use Case)

def str_out_function(val):
    def inner():
        print(f"{val}")

    inner()


str_out_function("Str")

# Lambda functions (short, anonymous functions)

# Simple lambda example
addition = lambda a, b: a + b
print(addition(1, 2))  # Output: 3

# Lambda with map function
my_list = [1, 2, 3, 4, 5, 6]
map_list = list(map(lambda n: 2 ** n, my_list))
for i in map_list:
    print(i)

# Filter example: keep even numbers
filter_list = list(filter(lambda i: (i % 2 == 0), my_list))
for i in filter_list:
    print(i)

# Reduce example: sum up values
import functools as ft

i = ft.reduce(lambda x, y: x + y, my_list)
print(i)  # Output: 21


# Function Annotations
# Add metadata to function arguments and return types using annotations.

def print_vat(**kwargs: 'VAT, gross and message'):
    print(kwargs)


print(print_vat.__annotations__)


def slice(string: str, start: int, end: int) -> str:
    return string[start:end]


# Global vs Local Variables
# Variables in functions are local by default. Use 'global' to modify them globally.

var = 1
result = 3


def scope_test():
    global result
    result = 5


scope_test()
print(result)  # Output: 5


# Nonlocal Variables
# The nonlocal keyword allows you to modify a variable from an outer function.

def myfunc1():
    x = "John"

    def myfunc2():
        nonlocal x
        x = "Mike"

    myfunc2()
    return x


print(myfunc1())  # Output: Mike


# Handling Variable-Length Arguments (*args)
# The *args syntax allows a function to accept a variable number of positional arguments.

def simple_args(*args):
    print(args)


simple_args(1, 2, 3)  # Output: (1, 2, 3)
