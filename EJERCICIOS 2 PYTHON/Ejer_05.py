'''
5. Crear una lista con los cuadrados de los números del 1 al 10
Usa un bucle para crear una lista que contenga los cuadrados de los números del 1 al 10.

'''
numeros = []
for i in range(1,10):
    numero = i ** 2
    numeros.append(numero)
    
print(f"Los números introducidos elevados al cuadrado son : {numeros}")