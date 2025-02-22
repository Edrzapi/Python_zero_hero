# Further Error Handling: Creating Custom Exceptions

# Creating a Custom Exception Class
class CustomError(Exception):
    """Base class for custom exceptions."""
    pass


class InvalidAgeError(CustomError):
    """Raised when the provided age is invalid."""

    def __init__(self, age):
        self.age = age
        self.message = f"The provided age '{age}' is not valid!"
        super().__init__(self.message)


# Using the Custom Exception
def check_age(age):
    if age < 0:
        raise InvalidAgeError(age)
    elif age < 18:
        print("You are underage.")
    else:
        print("You are an adult.")


try:
    check_age(-5)  # This will raise the custom exception
except InvalidAgeError as e:
    print(f"Custom Exception Caught: {e}")


# More advanced: chaining exceptions
class DatabaseError(Exception):
    """Custom exception for database errors."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class DatabaseConnectionError(DatabaseError):
    """Raised when there is an issue connecting to the database."""
    pass


try:
    raise DatabaseConnectionError("Failed to connect to the database!")
except DatabaseConnectionError as e:
    print(f"Database Error: {e}")
