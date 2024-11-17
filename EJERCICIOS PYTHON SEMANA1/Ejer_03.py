'''
Escribe un programa que lea un número entero y determine si es
positivo, negativo o cero.
'''

num1 = int(input("Ingrese un número entero"))
if num1 > 0:
    print(f"El número introducido es positivo")
elif num1 < 0:
    print(f"El número introducido es negativo")
else:
    print(f"El número introducido es 0")
