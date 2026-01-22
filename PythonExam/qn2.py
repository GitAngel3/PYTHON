#Write a program to enter a number and print its multiplication table till 10 rows.

n=int(input("Enter the no:"))


i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

