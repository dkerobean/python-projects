#operation functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What is the first number? "))
    #print all operations
    for key in operators:
        print(key)

    should_continue = True

    while should_continue:
        operation = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))
#get name of operation and set as a function
        calculation_function = operators[operation]
        result = calculation_function(num1, num2)

        print(f"{num1} {operation} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation: ") == "y":
            num1 = result
        else:
            should_continue = False
            calculator()


calculator()