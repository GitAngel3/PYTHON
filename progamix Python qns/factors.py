# Loop through range of numbers from 1 to 30.
# Print 3 if no. is multiple of 3.
# Print 5 if num is multiple of 5 and else print when num is neither mul of 3 or 5 

for i in range(1,31):
    if (i%3==0 and i%5==0): 
        print('3 & 5')
        
    elif (i%5==0):
        print(5)
    elif (i%3==0):
        print(3) 
         
    else:
        print(i)
    
        