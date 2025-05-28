'''
Clase:        Fundamentos de Programacion G2
Tema:         Bloque condicional
Ejercicio:    2.4.2
Descripción:  Numero mágico.

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-05-18
Estado:       [Terminado]
'''

Numero = int(input("Ingrese un numero: "))

if Numero % 7 == 0 and Numero % 5 != 0:
    print("Magico")
else:
    print("Normal")