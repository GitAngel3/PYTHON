

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


calc = Calculator()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", calc.add(num1, num2))
print("Subtraction:", calc.subtract(num1, num2))
print("Multiplication:", calc.multiply(num1, num2))
print("Division:", calc.divide(num1, num2))


"""
class Calculator:
    def __init__(self):
        self.a = int(input("Enter 1st number: "))
        self.b = int(input("Enter 2nd number: "))

    def calculate(self):
        add = self.a + self.b
        sub = self.a - self.b
        mul = self.a * self.b
        div = self.a / self.b

        print(f"{self.a} + {self.b} = {add}")
        print(f"{self.a} - {self.b} = {sub}")
        print(f"{self.a} * {self.b} = {mul}")
        print(f"{self.a} / {self.b} = {div}")


# create object
calc = Calculator()
calc.calculate()"""
