


# Ask user to enter a new item
item = input("Enter a new stationery item: ")

# Open file in append mode (creates file if it doesn't exist)
with open("items.txt", "a") as file:
    file.write(item + "\n")

print("\nUpdated list of stationery items:")

# Read and display all items
with open("items.txt", "r") as file:
    items = file.read()
    print(items)
