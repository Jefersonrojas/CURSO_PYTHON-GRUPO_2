'''
Escribe un programa que solicite al usuario un número entero y calcule
si es divisible por 3 y por 5.
'''

num1 = int(input("Ingrese un número entero "))
if num1%3 == 0:
    print(f"Si es divisible entre 3")
else:
    print(f"No es divisible entre 3")
    
if num1%5 == 0:
    print(f"Si es divisible entre 5")
else:
    print(f"No es divisible entre 5")
    