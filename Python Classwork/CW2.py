"""
You work for a bookstore that generates receipts for customers. 
Your task is to prepare a simple receipt using string techniques.
Here’s what you need to do:
Create a multiline string to store the receipt header.
The customer bought 2 items:
Book Title: "Python Basics" – ₹450
Book Title: "Data Science Intro" – ₹600
For each line showing the book and price, use a single string with basic
{} placeholders and call format() once to fill in the values.
Calculate the total price and add it similarly.
Concatenate a thank-you message at the end.
Make sure the output uses newline (\n) and tab (\t) for readability.
Display the entire receipt in uppercase.

"""
# work for a bookstore that generates receipts for customers
header ="""\t\t BOOKSTORE RECEIPT
\t\t SCHOLARS BOOK DEPOT
\t\t Textbooks • Reference • Notes
\t\t Near Govt School, City
\t\t Contact: 9XXXXXXXXX
\t\t----------------------------"""

book1="Python Basics"
b1_price=450

book2="Data Science Intro"
b2_price=600


line1="\n\tThe book :\t{} \t price: \t₹{}".format(book1,b1_price)
line2="\n\tThe book :\t{} \t price: \t₹{}".format(book2,b2_price)

total_price=b1_price+b2_price

total="\t\n Total price : \t\t₹{}".format(total_price)
thanks='\n\n\t\t  THANK YOU, Shop again!'

final= header+line1+line2+total+thanks
print(final.upper())

