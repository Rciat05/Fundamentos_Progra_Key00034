'''
Clase:        Fundamentos de Programacion G2
Tema:         Bloques iterativos
Ejercicio:    5.4.1
Descripción:  Adivina el numero

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-05-31
Estado:       [Terminado]
'''


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

