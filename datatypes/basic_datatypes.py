# Integer (int)
my_int = 10  # An integer value
print("Integer:", my_int)  

# Floating-Point (float)
my_float = 10.5  # A floating-point number
print("Float:", my_float)  

# Boolean (bool)
my_bool = True  # A boolean value (True or False)
print("Boolean:", my_bool)  

# String (str)
my_str = "Hello, World!"  # A string (sequence of characters)
print("String:", my_str)  

# Concatenating Different Data Types into Strings (Old Approach)
# Old concatenation method using '+' (string + string)
concatenated_str = "Integer: " + str(my_int) + ", Float: " + str(my_float)
print(concatenated_str)  # Concatenate integer and float with string conversion

# String Formatting Methods
# Using .format() (Old-style formatting)
formatted_str = "Integer: {}, Float: {}, Boolean: {}, String: {}".format(my_int, my_float, my_bool, my_str)
print(formatted_str)  # Using .format() method to format strings

# F-String - (A Cleaner Approach)
f_string = f"Integer: {my_int}, Float: {my_float}, Boolean: {my_bool}, String: {my_str}"
print(f_string)  # Using f-string for more readable string interpolation


# Function Returning a String
def my_function() -> str:
    return "This is a string from a function!"


# Calling the function and printing the return value
returned_str = my_function()
print("Returned String from Function:", returned_str)  # Output: String returned from the function

# The returned value from the function is treated as a string type
print("The type of the returned value is:", type(returned_str))  # This will print: <class 'str'>

# Type Conversion Between Data Types

# Converting float to integer
converted_int = int(
    my_float)  # Converts float to int - Remember, this is called narrowing, we have potential to lose details
print("Converted Float to Integer:", converted_int)

# Converting integer to float
converted_float = float(my_int)  # Converts integer to float - Remember, this is called widening, mostly safe
print("Converted Integer to Float:", converted_float)

# Converting boolean to integer (True -> 1, False -> 0)
converted_bool_to_int = int(my_bool)
print("Converted Boolean to Integer:", converted_bool_to_int)
