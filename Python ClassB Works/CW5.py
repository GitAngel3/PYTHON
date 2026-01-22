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
# 1. Create sets for each course
python_students = {"Asha", "Ravi", "Neha"}
data_science_students = {"Neha", "Karan", "Pooja"}

# 2. Add a new student to Python
python_students.add("Arjun")

# 3. Remove one student from Data Science
data_science_students.remove("Pooja")

# 4. Students enrolled in BOTH courses
both_courses = python_students & data_science_students
print("Students in both courses:", both_courses)

# 5. Students only in Python (not in Data Science)
only_python = python_students - data_science_students
print("Only Python students:", only_python)

# 6. All students in either course (no duplicates)
all_students = python_students | data_science_students
print("All students:", all_students)

# 7. Create dictionary with course names and student count
course_counts = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

# 8. Print course details using a loop
for course, count in course_counts.items():
    print(f"Course: {course}, Students: {count}")

# 9. Dictionary comprehension to double values
expected_growth = {course: count * 2 for course, count in course_counts.items()}
print("Expected growth:", expected_growth)
