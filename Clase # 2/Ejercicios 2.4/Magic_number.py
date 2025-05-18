Numero = int(input("Ingrese un numero: "))

if Numero % 7 == 0 and Numero % 5 != 0:
    print("Magico")
else:
    print("Normal")