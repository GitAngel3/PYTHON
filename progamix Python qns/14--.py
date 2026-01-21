# Program to check if a number is prime or not 
 

A = int(input("Enter a number: ")) 
 
flag = False 
 
if A == 1: 
    print(A, "is not a prime number") 
elif A > 1: 
  
    for i in range(2, A): 
        if (A % i) == 0: 
            flag = True 
            break 
            
    if flag: 
        print(A, "is not a prime number") 
    else: 
        print(A, "is a prime number")