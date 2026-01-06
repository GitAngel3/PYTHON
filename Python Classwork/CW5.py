"""You are managing an online course portal that keeps track of student enrollments in two subjects: "Frontend" and "Backend".
Create two sets:
One with the names of students enrolled in the Frontend course
One with the names of students enrolled in the Backend course
Perform the following tasks:
Add a new student to the Backend course
Remove a student from the Frontend course
Display the list of students who are enrolled in both courses
Display the list of students who are enrolled only in Backend, but not in Frontend
Display the total number of unique students
Create a dictionary where:
Keys are course names ("Frontend", "Backend")
Values are the number of students enrolled in each
Print each course name with the number of students using a loop
Using dictionary comprehension, create a new dictionary that adds a "Fullstack" course by combining student counts from both existing courses.

"""
Frontend = set(("Anu", "Jhansi", "Sreedevi","Helen"))
Backend = set(("John", "Manu", "Kumar","kavya"))
Backend.add("Ramya")
Frontend.remove("Sreedevi")
Frontend.discard("Sreedevi")# to avoid error if element not present in list

Frontend.update(Backend)
print(Frontend)
set_3 = Frontend.union(Backend)

#Display the list of students who are enrolled only in Backend, but not in Frontend
only_backend = Backend - Frontend
print(only_backend)

#Display the total number of unique students
total_unique_students = len(set_3)


course_counts = {
    "frontend": len(Frontend),
    "backend": len(Backend)
}

for course, count in course_counts.items():
    print(course, ":", count)


updated_courses = {
    **course_counts,
    "Fullstack": course_counts["Frontend"] + course_counts["Backend"]
}

# Output results
print("Frontend Students:", Frontend)
print("Backend Students:", Backend)
print("Students in both courses:", set_3)

print("Total unique students:", total_unique_students)
print("Updated course dictionary:", updated_courses)