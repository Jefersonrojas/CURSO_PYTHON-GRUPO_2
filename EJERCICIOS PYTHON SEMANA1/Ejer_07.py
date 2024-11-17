'''
Escribe un programa que solicite al usuario un número entero y
determine si es par o impar.
'''

num1 = int(input("Ingrese un número entero "))
if num1%2 == 0:
    print(f"El número ingresado es par")
else:
    print(f"El número ingresado es impar")