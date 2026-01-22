
def add_fn(a,b):
    sum=a+b

def mul_fn():
    x=add_fn*10
    return x
    
def print_fn():
    print('product of 10 and (sum of a and b) is:',mul_fn())
 
  
e=print_fn()
print(e)
