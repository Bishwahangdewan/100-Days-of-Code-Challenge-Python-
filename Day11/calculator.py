# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What is the first number? "))
    num2 = float(input("What is the second number? "))

    for symbols in operations:
        print(symbols)

    operation_symbol = input("Pick an operation from above ")
    function = operations[operation_symbol]
    answer = function(num1, num2)
    print(f"{num1}{operation_symbol}{num2} = {answer}")

    flag = 1

    while flag:
        operation_symbol = input("Pick another operation above from above ")
        num3 = float(input("What is the next number? "))
        function = operations[operation_symbol]
        answer = function(answer, num3)
        print(f"{answer}{operation_symbol}{num3} = {answer}")

        again = input("Do you want to Continue ? 'Yes' or 'No' ")

        if again == 'no':
            flag = False
            calculator()

calculator()
