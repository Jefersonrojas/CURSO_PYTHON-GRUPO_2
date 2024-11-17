'''
4.  Contar números pares e impares en un array
Haz un programa que cuente cuántos números pares e impares hay en una lista.

'''

cantidadNumeros = int(input(f"ingrese la cantidad de números a ingresar "))
numeros = []

for i in range(cantidadNumeros):
    numero = float(input(f"ingrese el número {i + 1} de {cantidadNumeros}: "))
    numeros.append(numero)
    
par, impar = 0, 0
for n in numeros:
    if n % 2==0:
        par +=1
    else:
        impar +=1
        
print(f"Cantidad de números pares es: {par}")
print(f"Cantidad de números impares es: {impar}")