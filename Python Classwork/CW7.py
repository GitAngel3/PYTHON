"""You are helping a shopper manage their grocery shopping list. Your task is to create a simple Python program 
that does the following steps in order:

Initial Grocery List:
Create a list with the initial items: ["milk", "bread", "eggs"].
Add Item Function:
  Write a function add_item(item) that adds a given item (string) to the grocery list.
Remove Last Item Function:
  Write a function remove_last_item() that removes the last item from the grocery list.
Lambda Function for Display:
Use a lambda function to print each item in the list with the format: "Item: <item>".
Recursive Character Count (Bonus):
Write a recursive function count_characters(items) that returns the total number of characters in all item names combined. 
For example, ["milk", "bread"] has 4 + 5 = 9 characters.."""

# helping a shopper manage their grocery shopping list.
grocery_list=["milk", "bread", "eggs"] 
def add_item(item):
    grocery_list.append(item)
    print(grocery_list)
    

 
#Use a lambda function to print each item in the list with the format: "Item: <item>"
display_item = lambda item: print(f"Item: {item}")

for item in grocery_list:
    print(display_item(item))
    

def count_characters(items):
    if not items:         
        return 0
    return len(items[0]) + count_characters(items[1:])
        
total_chars = count_characters(grocery_list)
print("Total characters:", total_chars)
    
add_item("Butter")  


def remove_last():
    if grocery_list:
        grocery_list.pop()
        print(grocery_list)
remove_last()
        
        
    
    
    
    
