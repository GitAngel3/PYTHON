"""Simple Calculator
Take two numbers as input and perform:

addition

subtraction

multiplication

division
Print the result and its datatype."""


a, b = input("Enter two numbers: ").split()
a = int(a)
b = int(b)


"""a=int(input('enter 1st no:'))
b=int(input('enter 2nd no:'))"""
add= a+b
sub= a-b
mul= a*b
div= a/b

print('a+b',add,type(add))
print('a-b',sub,type(sub))
print('a*b',mul,type(mul))
print('a/b',div,type(div))