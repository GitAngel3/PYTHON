# Multiline string for receipt header
header = """\tBOOKSTORE RECEIPT
\t------------------"""

# Item details
book1 = "Python Basics"
price1 = 450

book2 = "Data Science Intro"
price2 = 600

# Receipt lines using {} placeholders and format() once per line
line1 = "\n\tBOOK: {}\tPRICE: ₹{}".format(book1, price1)
line2 = "\n\tBOOK: {}\tPRICE: ₹{}".format(book2, price2)

# Calculate total
total = price1 + price2
total_line = "\n\tTOTAL AMOUNT:\t₹{}".format(total)

# Thank-you message
thank_you = "\n\n\tTHANK YOU FOR SHOPPING WITH US!"

# Combine everything and convert to uppercase
receipt = (header + line1 + line2 + total_line + thank_you).upper()

# Display receipt
print(receipt)


