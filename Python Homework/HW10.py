"""You are building a simple blueprint for different types of website users (like Admins and Guests). Each user must have a name and an account creation year.
Create a general User class with a constructor that stores the user's name and account year.
Mark User as an abstract class using a special decorator so no object can be created from it directly.
Add a concrete method account_age() that returns how many years old the account is (assume current year is 2025).
Add an abstract method get_role() that must be defined by every subclass.
Create two subclasses: Admin and Guest. Each should define their own version of get_role() returning 'Admin' and 'Guest' respectively.
Also, demonstrate the use of a magic method __str__() in each subclass to print a user-friendly message.
Create objects for both subclasses and print their role, account age, and object message using print()
"""
from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    def account_age(self):
        return 2025 - self.account_year

    # Abstract method
    @abstractmethod
    def get_role(self):
        pass



class Admin(User):
    def get_role(self):
        return "Admin"

    def __str__(self):
        return f"{self.name} is an Admin user."


class Guest(User):
    def get_role(self):
        return "Guest"

    def __str__(self):
        return f"{self.name} is a Guest user."


admin_user = Admin("Alice", 2018)
guest_user = Guest("Bob", 2022)


print(admin_user.get_role())
print(admin_user.account_age())
print(admin_user)

print()

print(guest_user.get_role())
print(guest_user.account_age())
print(guest_user)
