# Menu console
def show_menu():
    print("\nChoose an operation:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    print("Type 'quit' to exit.")


# Get operation
def get_operation():
    operation = input("Enter operation (+, -, *, /) or 'quit' to quit: ")
    return operation.strip().lower()


# Get numbers
def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid numbers.")


# Perform the operation
def perform_operation(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            return None
        return num1 / num2
    else:
        print("Invalid operation!")
        return None


# Runner
def run():
    while True:
        show_menu()
        operation = get_operation()

        if operation == 'quit':
            print("Goodbye!")
            break

        num1, num2 = get_numbers()

        result = perform_operation(operation, num1, num2)

        if result is not None:
            print(f"Result: {result}")
