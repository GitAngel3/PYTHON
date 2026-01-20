"""Create a program for a mini library system that asks the user to enter a book title and publication year.
If the book title contains only alphabets and spaces, accept it. Otherwise, show an error.
The publication year must be a 4-digit number starting with “19” or “20”. If not, display an error.
Use appropriate error handling to catch any invalid inputs and ensure a message is printed at the end whether or not there was an error.

"""
# Mini Library System
import re

title_pattern = r'^[A-Za-z ]+$'
year_pattern = r'^(19|20)\d{2}$'

try:
    title = input("Enter a book title: ")

    
    if not re.fullmatch(title_pattern, title):
        raise ValueError("Book title must contain only alphabets and spaces")

    year = input("Enter the publication year: ")

   
    if not re.fullmatch(year_pattern, year):
        raise ValueError("Year must be a 4-digit number starting with 19 or 20")

except ValueError as e:
    print("Error:", e)

else:
    print("Title accepted")
    print("Year accepted")
    print("Book Title:", title)
    print("Publication Year:", int(year))
