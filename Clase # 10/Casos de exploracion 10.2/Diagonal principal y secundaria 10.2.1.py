
'''
Clase:        Fundamentos de Programacion G2
Tema:         Manejo de matrices
Ejercicio:    10.2.1
Descripción:  Diagonal Principal y Secundaria

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-06-03
Estado:       [En progreso]
'''

N = int(input("Ingrese la matriz: "))
matriz = []

for i in range(N):
    temp = list(map(int, input().split()))
    matriz.append(temp)

