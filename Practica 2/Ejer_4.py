print("Bienvenido a la sala de juego")
try:
    edad= int(input("Cual es su edad? "))
except Exception:
    print("valor ingresado invalido")
precio = float("0")

if edad>0 and edad <4:
    precio = 0
elif edad >=4 and edad <= 18:
    precio = 5
elif edad > 18:
    precio = 10
else:
    print("edad no puede ser negativo o 0")
    
print(f"El precio de la entrada es: {precio}")