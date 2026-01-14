

#string methods
a = "Mashup, Stack!"
b = a.capitalize()  #1st lettter to capital
print(b)

a = "MASHUP!"
b = a.casefold()     #Returns given srring in lowercase
print(b)

a = "Mashup, Stack!"
b = a.count('a')
print(b)

a = "Mashup, Stack!"
b = a.center(30)   #justify string to centre-if position(width argument) is given as an argument
print(b)

a = "Mashup, Stack!"
b = a.encode()
print(b)

a = "Mashup, Stack!"
b = a.endswith("k")
print(b)  