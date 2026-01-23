"""Simple Calculator
Take two numbers as input and perform:

addition

subtraction

multiplication

division
Print the result and its datatype."""


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