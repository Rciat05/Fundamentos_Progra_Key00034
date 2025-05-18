Anio = int(input("Ingrese un anio: "))

if Anio % 4 == 0 and Anio % 100 != 0:
    print("Bisiesto")
elif Anio % 400 == 0:
    print("Bisiesto")
else:
    print("No bisiesto")