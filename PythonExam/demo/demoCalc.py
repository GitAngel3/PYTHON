

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
calc.calculate()
