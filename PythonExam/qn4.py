#Create a calculator program using OOPS.
# Make sure you create a class Calculator and 
# then use its object to access the calculator operations such as addition, 
# subtraction, division and multiplication.

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b

calc = Calculator()

a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))


if operator == "+":
    print("Result:", calc.add(a, b))
elif operator == "-":
    print("Result:", calc.subtract(a, b))
elif operator == "*":
    print("Result:", calc.multiply(a, b))
elif operator == "/":
    print("Result:", calc.divide(a, b))
else:
    print("Invalid operator!")
