'''
Clase:        Fundamentos de Programacion G2
Tema:         Manejo de matrices
Ejercicio:    10.2.1
Descripción:  Diagonal Principal y Secundaria

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-06-03
Estado:       [Terminado]
'''

N = 4
matriz = []
Diagonal1 = []
Diagonal2 = []

print("Ingrese los valores de la matriz 4x4, fila por fila:")
for i in range(N):
    fila = list(map(int, input(f"Fila {i+1}: ").split()))
    while len(fila) != N:
        print("Error: la fila debe tener exactamente 4 elementos.")
        fila = list(map(int, input(f"Fila {i+1} (nuevamente): ").split()))
    matriz.append(fila)

print("\nMatriz ingresada:")
for fila in matriz:
    print(fila)

print("\nDiagonal principal:")
for i in range(N):
    for j in range(N):
        if i == j:
            Diagonal1.append(matriz[i][j])
print(Diagonal1)

print("\nDiagonal secundaria:")
for i in range(N):
    for j in range(N):
        if i + j == N - 1:
            Diagonal2.append(matriz[i][j])
print(Diagonal2)



