"""Homework Problem:
A local school wants to keep track of students' names in a file.

Ask the user how many student names they want to add.

Then, take that many names as input and store each name on a new line in a file called students.txt.

If the file already exists, first show all existing names, then add the new ones without removing the old ones.

After saving the new names, read and display the updated list of all student names."""



n= int(input('Enter the count of student names you want to add:'))


for i in range(n):
    names = []
    name = input(f"Enter names {i+1}: ")
    names.append(name)

print("List of names:", names)




f = open("students.txt", "a")
f.write(item)
f.close()
f=open("items.txt", "r")
print("\nUpdated list of stationery items:")
print(f.read())


