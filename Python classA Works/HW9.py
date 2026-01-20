"""You are helping a bank manage different types of bank accounts. Your task is to create a simple Python program that does the following steps in order:
Create a base class called Account with an account holder's name (string) and balance (number, like 1000.0). Use a single underscore to keep the name and balance protected.
Create a class called SavingsAccount that inherits from Account and has a method calculate_interest that returns the interest as balance * 0.05 (5% interest).
Create a class called CurrentAccount that inherits from Account and has a method calculate_interest that returns the interest as balance * 0.02 (2% interest).
Add a special method to the Account class so that using the + operator on two accounts adds their balances together.
In the main part of the program:
Create a SavingsAccount object for "Ravi" with a balance of 10000.
Create a CurrentAccount object for "Anjali" with a balance of 15000.
Show the name, balance, and interest for each account object.
Show the total balance by adding the two account objects using the + operator.
Make the output clear, showing each account’s name, balance, interest, and the total balance.

"""

class Account:
    def __init__(self, name, balance):
        self._name = name       
        self._balance = balance 

  
    def __add__(self, other):
        return self._balance + other._balance



class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05  # 5% interest



class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02  # 2% interest



savings = SavingsAccount("Ravi", 10000)

print("Savings Account Details:")
print(f"Name: {savings._name}")
print(f"Balance: {savings._balance}")
print(f"Interest: {savings.calculate_interest()}")

print("\nCurrent Account Details:")
print(f"Name: {current._name}")
print(f"Balance: {current._balance}")
print(f"Interest: {current.calculate_interest()}")


total_balance = savings + current
print("\nTotal Balance (Savings + Current):", total_balance)
