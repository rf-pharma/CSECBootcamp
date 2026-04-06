def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("Welcome to My CLI Calculator!")
    print("Available operations: +  -  *  /")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    while True:
        op = input("Enter operation (+ - * /): ")
        if op == "+":
            result = add(a, b)
            break
        elif op == "-":
            result = subtract(a, b)
            break
        elif op == "*":
            result = multiply(a, b)
            break
        elif op == "/":
            result = divide(a, b)
            break
        else:
            print("Invalid operation! Please try again.")

    print(f"The result of {a} {op} {b} is: {result}")

calculator()