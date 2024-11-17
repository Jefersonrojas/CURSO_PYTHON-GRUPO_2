'''
Escribe un programa que tome una calificación numérica de un
estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Menos de 60: F
'''

num1 = float(input("Ingrese un número entero"))
if 100 >= num1 and  num1 >= 90:
    print("A")
elif 89 >= num1 and  num1 >= 80:
    print("B")
elif 79 >= num1 and  num1 >= 70:
    print("C")
elif 69 >= num1 and  num1 >= 60:
    print("D")
elif num1 < 60:
    print("F")