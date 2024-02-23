def calcular_factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else: 
        return numero * calcular_factorial(numero - 1)

if __name__ == "__main__":
    numero = int(input("ingrese un numero para calcular su factorial: "))
    resultado = calcular_factorial(numero)
    print(f"el factorial de {numero} es {resultado}")

