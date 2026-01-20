"""You are helping to create a simple name game for a birthday event.
Ask the user to enter a list of names of invited guests (comma-separated).
Remove any duplicate names.
Randomly choose one name from the final list to play a game.
Reverse the selected name and display it.
Also, print the total number of unique names and round the square root of that number to the nearest whole number.
"""

import random
names=input('enter a list of names of invited guests with coma-seperated ').split(",")



print ("The original list is : " +  str(names)) 

result = [] 
for x in names: 
    if x not in result: 
        result.append(x) 

print ("The list after removing duplicates : " + str(result)) 





sampling = random(names)
print("sampling with choices method ", sampling)




import random
import math

# Ask user to enter comma-separated names
names_input = input("Enter the names of invited guests (comma-separated): ")

# Convert input string to list and remove extra spaces
names_list = [name.strip() for name in names_input.split(",")]

# Remove duplicate names using set, then convert back to list
unique_names = list(set(names_list))

# Randomly choose one name
chosen_name = random.choice(unique_names)

# Reverse the chosen name
reversed_name = chosen_name[::-1]

# Count unique names
count_unique = len(unique_names)

# Round the square root of the count
rounded_sqrt = round(math.sqrt(count_unique))

# Display results
print("\n🎉 Birthday Name Game Results 🎉")
print("Unique Names:", unique_names)
print("Randomly Selected Name:", chosen_name)
print("Reversed Name:", reversed_name)
print("Total Unique Names:", count_unique)
print("Rounded Square Root of Count:", rounded_sqrt)
