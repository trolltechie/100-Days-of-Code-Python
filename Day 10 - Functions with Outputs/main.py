import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# summarize = add
# minus = subtract
# times = multiply
# divided = divide

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    first_number = float(input("Enter first number: "))
    should_accumulate = True
    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        second_number = float(input("Enter second number: "))

        calculating_function = operations[operation_symbol]
        answer = calculating_function(first_number, second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {answer}")

        should_continue = input(f"Would you like to use another operation? Type 'yes' to continue calculating with {answer} or 'no' to start from beginning ").lower()
        if should_continue == "yes":
            first_number = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()