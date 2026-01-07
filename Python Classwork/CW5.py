"""you are creating a basic system to manage students enrolled in various courses.
Create two sets: one for students enrolled in "Python" and one for "Data Science".
Add a new student to the Python set.
Remove one student from the Data Science set.
Find and display the names of students who are enrolled in both courses.
Find students who are only in the Python course but not in Data Science.
Display the combined list of all students in either course (no duplicates).
Create a dictionary with course names as keys and number of students as values.
Using a loop, print the course name and number of students in the format:
Course: Python, Students: 3
Using dictionary comprehension, create a new dictionary where course names are unchanged, but values are doubled (to simulate expected growth)


"""
Python = set(("Anu", "Jhansi","kavya", "Sreedevi","Helen"))
Data_Science = set(("John", "Manu","Jhansi", "Kumar","kavya"))
print(Python & Data_Science)
print(Python-Data_Science)
print(Python|Data_Science)
course_counts = {
    "Python": len(Python),
    "Data_science": len(Data_Science)
}
for x, y in course_counts.items():
  print(x,':',y)
#Using dictionary comprehension, create a new dictionary where course names are unchanged, but values are doubled (to simulate expected growth)

double_length = {course_counts: 2*len()}
print(double_length)




