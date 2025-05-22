'''
Clase:        Fundamentos de Programacion G2
Tema:         Bloque condicional
Ejercicio:    2.4.1
Descripción:  Año bisiesto

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-05-18
Estado:       [Terminado]
'''


Anio = int(input("Ingrese un anio: "))

if Anio % 4 == 0 and Anio % 100 != 0:
    print("Bisiesto")
elif Anio % 400 == 0:
    print("Bisiesto")
else:
    print("No bisiesto")