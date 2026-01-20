# Python Program to find the area of triangle

a,b,c=map(float,input('Enter 2 sides of triangle using comas=').split(','))

def area_tri(a,b,c):
    s=0.5*(a+b+c)
    A=(s*(s-a)*(s-b)*(s-c))**0.5
    return A
    
print("Area =", area_tri(a, b, c))