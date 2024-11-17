'''
Escribe un programa que solicite al usuario dos números y muestre su
suma, resta, multiplicación, división, división entera y residuo (módulo).
'''

num1, num2=0,0
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")

# Realizar las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "Error: División por cero"
division_entera = num1 // num2 if num2 != 0 else "Error: División por cero"
residuo = num1 % num2 if num2 != 0 else "Error: División por cero"

# Mostrar los resultados
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicación es: {multiplicacion}")
print(f"La división es: {division}")
print(f"La división entera es: {division_entera}")
print(f"El residuo es: {residuo}")