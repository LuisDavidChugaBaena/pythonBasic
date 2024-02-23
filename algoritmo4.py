n = int(input("ingresa un numero"))
x = 1
c = 0
while x <= n:
    if n % x == 0:
        c = c + 1
    x = x + 1
if c == 2: 
    print("el numero",n,"es primo")
else:
    print("el numero",n,"no es primo")