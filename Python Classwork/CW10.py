"""You are building a basic user account system. Every user has a name and a year they joined. Your task is to:
Create a general User class that cannot be used directly to make objects, but stores name and joining year.
Add a method to calculate how many years the user has been on the platform (assume current year is 2025).
Add two types of users: Customer and Vendor, each showing their specific role when asked.
Use a special print message for each user that shows their name, role, and how many years they’ve been using the platform.
"""
#User Account system

from abc import ABC, abstractmethod 
current_year=2025
  
class User(ABC):
    def __init__(self,name,year): 
      self.name = name
      self.year = year
    def calc_year(self):
        return current_year-self.year
    @abstractmethod
    def get_role(self):
        pass

    def display_info(self):
        print(
            f"Name: {self.name} | "
            f"Role: {self.get_role()} | "
            f"Years on platform: {self.calc_year()}"
        )


class Customer(User):
    def get_role(self):
        return "Customer"


class Vendor(User):
    def get_role(self):
        return "Vendor"


user1 = Customer("Amit", 2020)
user2 = Vendor("Riya", 2018)

user1.display_info()
user2.display_info()



        
    
  
