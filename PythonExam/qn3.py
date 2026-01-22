# Consider the following array [(id:1, name:"rajesh"), (id:2, name: "rahul"}, {id:3, name: "sruthi"}]
#Write a program to accept a number and print the name of the student with that id

students = {
    1: "rajesh",
    2: "rahul",
    3: "sruthi"}

id=int(input("Enter the id of the student:"))

if id in students:
    print("Student name:", students[id])
else:
    print("Student ID is not found")
