edad= int(input("Cual es su edad? "))
ingresos= float(input("cuales son sus ingresos mensuales?"))
if edad >= 16  and ingresos >= 1000:
    print("Usted es apto para tributar ")
elif edad<16 and ingresos >=1000:
    print("Usted no es apto para tributar ya que apesar que sus ingresos sean mayores a lo establecido, es menor de edad ):")
elif edad >= 16 and ingresos < 1000:
    print("Usted no es apto para tributar ya que apesar que es mayor de edad sus ingresos no cumplen con lo establecido ):")
else:
    print("Usted no puede tributar")