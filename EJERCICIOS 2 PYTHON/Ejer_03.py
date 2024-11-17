'''
3.  Encontrar el número más grande en un array
Escribe un programa que determine el mayor número en una lista.

'''

cantidadNumeros = int(input(f"ingrese la cantidad de números a ingresar "))
numeros = []

for i in range(cantidadNumeros):
    numero = float(input(f"ingrese el número {i + 1} de {cantidadNumeros}: "))
    numeros.append(numero)
    
print(f"el número mayor de la lista es {max(numeros)}")    

