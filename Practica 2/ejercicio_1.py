'''1. Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
mayúsculas y minúsculas. (10 p)
'''

usuario = input("Ingrese contraseña: ")
contraseña= "Esthepancito"
if usuario == contraseña:
    print(f"contraseña coorecta, la contraseña correcta es {contraseña}.")
else:
    print("contraseña incorrecta")
    