'''
Escribe un programa que solicite al usuario tres números y determine
cuál de ellos es el mayor.
'''

numeros = []

for i in range(3):
    numero = float(float(input(f"ingrese el número {i + 1}: ")))
    numeros.append(numero)

numero_mayor = max(numeros)

print(f"Los números introducidos son: {numeros}")
print(f"El número mayor es: {numero_mayor}")