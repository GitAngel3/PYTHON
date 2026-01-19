"""You are helping to create a simple name game for a birthday event.
Ask the user to enter a list of names of invited guests (comma-separated).
Remove any duplicate names.
Randomly choose one name from the final list to play a game.
Reverse the selected name and display it.
Also, print the total number of unique names and round the square root of that number to the nearest whole number.
"""
names=input('enter a list of names of invited guests with coma-seperated ').split(",")



print ("The original list is : " +  str(names)) 

result = [] 
for x in names: 
    if x not in result: 
        result.append(x) 

print ("The list after removing duplicates : " + str(result)) 


import random


sampling = random(names)
print("sampling with choices method ", sampling)