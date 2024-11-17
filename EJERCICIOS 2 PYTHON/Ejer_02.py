'''
2. Sumar todos los elementos de un array
Crea un programa que tome una lista de números y calcule la suma de todos sus elementos.

'''
cantidadNumeros = int(input(f"ingrese la cantidad de números a ingresar "))
numeros = []

for i in range(cantidadNumeros):
    numero = float(input(f"ingrese el número {i + 1} de {cantidadNumeros}: "))
    numeros.append(numero)
    
print(f"la suma de los números es {sum(numeros)}")    



