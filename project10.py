logoo = """
_______________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________
"""
print(logoo)

def add (n1,n2):
    return n1 + n2

def subtract (n1,n2):
    return n1 - n2

def multiply (n1,n2):
    return n1 * n2

def divide (n1,n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2
operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
   
}
def calculator():
    accumulate = True
    num1 = float(input("What is  the first number? "))
    while accumulate:
        for symbol in operation:
            print(symbol)
        operation_symbol = input("pick an operation symbol? ")
        num2 = float(input("What is the second number? "))
        answer = operation[operation_symbol](num1, num2)
        print (f"{num1} {operation_symbol}  {num2} = {answer}")
        choice = input(f"type 'y' to continue with calculating with the {answer} or type 'n' to start a new calculation? ")
        if choice == "y":
            num1 = answer
        else:
            accumulate = False
            print("\n" *20)
            print(logoo)
            calculator()  

calculator()