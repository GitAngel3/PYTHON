#Create a calculator program using OOPS.
# Make sure you create a class Calculator and 
# then use its object to access the calculator operations such as addition, 
# subtraction, division and multiplication.

class calculator():
    a=int(input('enter 1st no:'))
    b=int(input('enter 2nd no:'))

   
    add= a+b
    sub= a-b
    mul= a*b
    div= a/b
    
    print(f'{a}+{b}=',add)
    print(f'{a}-{b}=',sub)
    print(f'{a}*{b}=',mul)
    print(f'{a}/{b}=',div)
    
    
calculator()