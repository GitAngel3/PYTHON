"""Homework Problem:
A local school wants to keep track of students' names in a file.

Ask the user how many student names they want to add.

Then, take that many names as input and store each name on a new line in a file called students.txt.

If the file already exists, first show all existing names, then add the new ones without removing the old ones.

After saving the new names, read and display the updated list of all student names."""




filename = "students.txt"

try:
    with open(filename, "r") as file:
        existing_names = file.read().strip()
        if existing_names:
            print("Existing student names:")
            print(existing_names)
        else:
            print("The file exists but is empty.")
except FileNotFoundError:
    print("No existing file found. A new file will be created.")


n = int(input("\nHow many student names do you want to add? "))

with open(filename, "a") as file:
    for i in range(n):
        name = input(f"Enter student name {i + 1}: ")
        file.write(name + "\n")

print("\nUpdated list of student names:")
with open(filename, "r") as file:
    print(file.read())
