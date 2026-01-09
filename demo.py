

a = input("Enter a number:")
if(int(a)%2 == 0):
	print("The number is even")
else:
 
 #qn 8
 
 class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def show_details():
      
      obj1 = Person("string", "integer")
      print(obj1.name)
      print(obj1.age)

class Employee(Person):
  def __init__(self, name, age,employee_id):
    self.name = name
    self.age = age
  def show_details():
      
      obj1 = Person("string", "integer")
      print(obj1.name)
      print(obj1.age)

  def working_hours (float):