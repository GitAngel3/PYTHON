"""A fitness center wants to create a simple system to define and display staff profiles based on their roles for record-keeping purposes. You are tasked with creating a Python program to represent different types of staff. Complete the following steps:

Define a base class Employee with attributes name (string) and role (string), and a method display() that prints the employee’s name and role.
Create a class Trainer that inherits from Employee, adds an attribute specialization (string), and includes a display() method to print the trainer’s name, role, and specialization.
Create a class YogaInstructor that inherits from Employee, adds an attribute yoga_style (string), and includes a display() method to print the yoga instructor’s name, role, and yoga style.
Create a class MultiTrainer that inherits from both Trainer and YogaInstructor, includes both specialization and yoga_style attributes, and has a display() method to print the multi-trainer’s name, role, specialization, and yoga style.
Create one object from each class (Employee, Trainer, YogaInstructor, MultiTrainer) with sample data.
Display the details of each object by calling its display() method"""

# Base class
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")


# Trainer class (inherits from Employee)
class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Specialization: {self.specialization}")


# YogaInstructor class (inherits from Employee)
class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Yoga Style: {self.yoga_style}")


# MultiTrainer class (inherits from Trainer and YogaInstructor)
class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Specialization: {self.specialization}")
        print(f"Yoga Style: {self.yoga_style}")


# Creating objects
employee = Employee("Ravi", "Front Desk Staff")
trainer = Trainer("Anil", "Gym Trainer", "Weight Training")
yoga_instructor = YogaInstructor("Meera", "Yoga Instructor", "Hatha Yoga")
multi_trainer = MultiTrainer("Sonia", "Multi Trainer", "Cardio Training", "Vinyasa Yoga")

# Displaying details
print("Employee Details:")
employee.display()
print("\nTrainer Details:")
trainer.display()
print("\nYoga Instructor Details:")
yoga_instructor.display()
print("\nMulti Trainer Details:")
multi_trainer.display()
