'''
2. Sumar todos los elementos de un array
Crea un programa que tome una lista de números y calcule la suma de todos sus elementos.
'''

cantidad = int(input("¿Cuántos números deseas ingresar? "))

suma_total = 0
suma_positivos = 0
suma_negativos = 0
contador_positivos = 0
contador_negativos = 0
contador_cero = 0

for i in range(cantidad):
    
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma_total += numero
    
    if numero > 0:
        suma_positivos += numero
        contador_positivos += 1
    elif numero < 0:
        suma_negativos += numero
        contador_negativos += 1
    else:
        contador_cero += 1 

print("\nResultados:")
print(f"Suma total de los números: {suma_total}")
print(f"Suma de los números positivos: {suma_positivos}")
print(f"Suma de los números negativos: {suma_negativos}")
print(f"Número de números positivos: {contador_positivos}")
print(f"Número de números negativos: {contador_negativos}")
print(f"Número de ceros: {contador_cero}")
    
if contador_positivos > 0:
    promedio_positivos = suma_positivos / contador_positivos
    print(f"Promedio de los números positivos: {promedio_positivos:.2f}")
else:
    print("No se ingresaron números positivos para calcular el promedio.")

if contador_negativos > 0:
    promedio_negativos = suma_negativos / contador_negativos
    print(f"Promedio de los números negativos: {promedio_negativos:.2f}")
else:
    print("No se ingresaron números negativos para calcular el promedio.")
