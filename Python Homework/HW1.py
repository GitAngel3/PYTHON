"""Homework Problem:
A grocery store wants to calculate the final bill for a customer. The store has 3 products: rice, sugar, and oil. Each product has a fixed price per kilogram:
Rice: ?45 per kg
Sugar: ?40 per kg
Oil: ?130 per kg
Assume a customer bought:
3 kg of rice
2.5 kg of sugar
1.8 kg of oil
Your task:
Use variables to store the prices and quantities.
Use appropriate data types.
Calculate and print the total price for each item and the final total bill.
Show the total bill as an integer and also as a string.
Convert the float values where needed using explicit conversion.
Use random number generation to add a random ?5–?10 delivery charge.
Show the final bill amount including delivery charge."""

Rice=45 
Sugar=40 
Oil=130 
Q1=3
Q2=2.5
Q3=1.8
price_of_rice= float(Rice*Q1)
price_of_sugar=float(Sugar*Q2)
price_of_oil=float(Oil*Q3)

final_total_bill=price_of_rice+price_of_sugar+price_of_oil

#show the total bill as an integer and also as a string.
print('price_of_rice=',price_of_rice)
print('price of sugar=',price_of_sugar)
print('price of oil=',price_of_oil)
print('final bill=',int(final_total_bill))
print('final bill=',str(final_total_bill))

import random
delivery_charge=random.randrange(5,10)
print('delivery charge=',delivery_charge)
final_bill = final_total_bill + delivery_charge
print('final bill amount including delivery charge=',final_bill)