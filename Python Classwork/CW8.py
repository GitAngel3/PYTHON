"""A company wants to create a simple system to define and display employee profiles based on their role types for record-keeping purposes.
You are tasked with creating classes to represent different types of individuals in Python. Complete the following steps:
Create a class Person with attributes name (string) and age (integer), and a method show_details() that prints the person’s name and age.
Create a class Employee that inherits from Person, adds an attribute employee_id (string), and includes a show_details() method to print the employee’s name, age, and employee ID.
Create a class PartTime that inherits from Person, adds an attribute working_hours (float), and includes a show_details() method to print the part-time worker’s name, age, and working hours.
Create a class Consultant that inherits from both Employee and PartTime, adds an attribute project_name (string), and includes a show_details() method to print the consultant’s name, age, employee ID, working hours, and project name.
Create one object of each class (Person, Employee, PartTime, Consultant) with sample data.
Display the details of each object by calling its show_details() method"""
    

      
      # Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Employee class inheriting from Person
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")


# PartTime class inheriting from Person
class PartTime(Person):
    def __init__(self, name, age, working_hours):
        super().__init__(name, age)
        self.working_hours = working_hours

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Working Hours: {self.working_hours}")


# Consultant class inheriting from Employee and PartTime
class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.working_hours = working_hours
        self.project_name = project_name

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Working Hours: {self.working_hours}")
        print(f"Project Name: {self.project_name}")


# Creating objects
person = Person("Ravi", 30)
employee = Employee("Anita", 28, "EMP101")
part_time = PartTime("Kiran", 22, 20.5)
consultant = Consultant("Suman", 35, "CONS501", 15.0, "AI Automation")

# Displaying details
print("\nPerson Details:")
person.show_details()

print("\nEmployee Details:")
employee.show_details()

print("\nPart-Time Worker Details:")
part_time.show_details()

print("\nConsultant Details:")
consultant.show_details()

      