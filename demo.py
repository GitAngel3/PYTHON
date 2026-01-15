


# Mini Library System
import re

pattern = r'^[A-Za-z ]+$'

try:
    title = input("Enter a book title: ")
    
    # validate title using regex
    if not re.fullmatch(pattern, title):
        raise ValueError("Book title must contain only alphabets and spaces")
    
    year = int(input("Enter the publication year: "))

except ValueError as e:
    print("Error:", e)

else:
    print("Title name accepted")
    print("Book Title:", title)
    print("Publication Year:", year)
