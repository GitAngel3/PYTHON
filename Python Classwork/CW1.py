#A juice shop sells three types of drinks: apple, orange, and grape. You are asked to calculate the total volume of juice sold in one day.
#The shop sold:
#15.5 liters of apple juice
#20 liters of orange juice
#10.25 liters of grape juice
#Your task:
#Store the volume of each juice in separate variables.
#Calculate the total volume sold.
#Print the total volume.
#Convert the total volume to an integer and print it.
#Convert the total volume to a string and print it with a message.
#Add a random number between 5 and 10 (representing additional bonus liters) and print the final total

a=15.5
b=20
c=10.25
total_vol=a+b+c
print('total volume=',total_vol)
e=int(total_vol)
print('total volume as integer=',e)
f=str(total_vol)
print('total volume as string is'+f)

import random

print('Additional bonus=',random.randrange(5, 10))
print('Final total volume=',total_vol+random.randrange(5, 10))




