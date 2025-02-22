# Introduction to Error Handling in Python

# Error handling in Python is done using the try-except block.

# Basic Try-Except Block
try:
    # Division by zero
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

# Catching Multiple Exceptions
try:
    num = int("Hello")  # This will raise a ValueError
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Using Else Block (Executes if no exception is raised)
try:
    value = 5
    result = value / 2
except ZeroDivisionError:
    print("Error: Division by zero.")
else:
    print(f"The result is: {result}")

# Finally Block (Always executes)
try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("Error: File not found!")
finally:
    print("This will always execute!")

# Raising Exceptions (manually)
try:
    raise ValueError("This is a custom error!")
except ValueError as e:
    print(f"Custom Error: {e}")
