"""You are creating a mini lucky draw system for a small online gift store.
Ask the user to enter names of customers (comma-separated) who have placed orders today.
Remove any duplicate names from the list.
Randomly shuffle the final list of names.
Pick and display 2 winners using random selection.
For fun, reverse the names of both winners before displaying.
Display the total number of unique participants.
Use the math module to show the square root of the number of participants, rounded to the nearest whole number.

"""
import random
import math

names_input = input("Enter names seperated by comas: ")

names = [name.strip() for name in names.split(",")]

# Step 3: Remove duplicate names using set, then convert back to list
unique_names = list(set(names_list))

# Step 4: Shuffle the list randomly
random.shuffle(unique_names)

# Step 5: Pick 2 winners (if possible)
if len(unique_names) < 2:
    print("Not enough participants to pick 2 winners.")
else:
    winners = random.sample(unique_names, 2)

    # Step 6: Reverse the names of winners
    reversed_winners = [winner[::-1] for winner in winners]

    print("\n Lucky Draw Winners ")
    print("Winner 1:", reversed_winners[0])
    print("Winner 2:", reversed_winners[1])

# Step 7: Display total number of unique participants
total_participants = len(unique_names)
print("\nTotal unique participants:", total_participants)

# Step 8: Square root of number of participants (rounded)
sqrt_participants = round(math.sqrt(total_participants))
print("Square root of participants (rounded):", sqrt_participants)
