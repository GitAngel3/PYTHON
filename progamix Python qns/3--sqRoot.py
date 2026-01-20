# Python Program to calculate the square root

import math

a = float(input('Enter 1st number, root should be found: '))
b = float(input('Enter 2nd number, root should be found: '))


def exp_pow_fn(a):  #using exponential power operator**
  sqr=a**0.5
  print('square root of \t{}=\t{}'.format(a,sqr))

def sqrt_fn(b):  # using math operator--math.sqrt()
  print('square root of \t{}=\t'.format(math.sqrt(b)))
  
exp_pow_fn(a)  
sqrt_fn(b)





