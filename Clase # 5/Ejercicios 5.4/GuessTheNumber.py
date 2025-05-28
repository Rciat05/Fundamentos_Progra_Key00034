import random 

Numero_Random = random.randint(1, 101)
numero_User = int(input("Ingrese un numero a adivinar entre 1 y 100: "))

while Numero_Random != numero_User:
        if Numero_Random < numero_User:
            print("El numero secreto es menor")
        elif Numero_Random > numero_User:
            print("El numero secreto es mayor")
        numero_User = int(input("Ingrese un numero a adivinar entre 1 y 100: "))

print("¡Felicidades! el número ingresado es correcto.")

