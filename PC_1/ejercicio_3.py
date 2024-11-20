renta= float(input("Cual es su renta anual: "))

if renta>0 and renta <10000:
    print("5%")
elif renta >=1000 and renta <= 2000:
    print("15%")
elif renta > 2000 and renta <= 35000:
    print("20%")
elif renta > 35000 and renta <= 60000:
    print("30%")
else:
    print("45%")
    
    