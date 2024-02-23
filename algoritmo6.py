def parOimpar(numero): 
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
    
numero = int(input("ingrese el numero"))
print("el numero es" ,parOimpar(numero))