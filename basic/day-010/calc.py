from arts import logo

# An approach was implemented to use a function management instead of several if/elif/else 
# to identify the operation selected by the user.
def sum_operation(a, b):
    return a + b

def subtract_operation(a, b):
    return a - b

def multiply_operation(a, b):
    return a * b

def divide_operation(a, b):
    return a / b if b != 0 else "Error: Cannot divide by zero"

OPERATIONS = {
    "+": sum_operation,
    "-": subtract_operation,
    "*": multiply_operation,
    "/": divide_operation,
}

print(logo)

def calc():
    number1 = float(input("Enter a number: "))

    should_continue = True
    while should_continue:
        operation = input("Pick and operation: \n+\n-\n*\n/\n")
        number2 = float(input("Enter another number: "))

        calculator = OPERATIONS[operation]
        result = calculator(number1, number2)

        print(f"{number1} {operation} {number2} = {result}")

        if input(f"Continue with {result} or start a new calculation? y/n: ") == "y":
            number1 = result
        else:
            calc()

calc()      
