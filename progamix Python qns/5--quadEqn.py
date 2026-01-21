# Solve the quadratic equation ax**2 + bx + c = 0
import math

def quad_fn():
    a = int(input('Enter 1st no:'))
    b = int(input('Enter 2nd no:'))
    c = int(input('Enter 3rd no:'))
    d = ((b*b)-4*a*c)
    soln_1=(-b+math.sqrt(d))/ (2 * a) #math.pow(b, 2) - 4 * a * c

    soln_2=(-b-math.sqrt(d))/ (2 * a)
    
    print('solution 1=%.2f'%soln_1)
    print('solution 2=%.2f'%soln_2)
    
quad_fn()