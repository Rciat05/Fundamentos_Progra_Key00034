'''
Clase:        Fundamentos de Programacion G2
Tema:         Manejo de matrices
Ejercicio:    10.3.1
Descripción:  Verifica si una matriz es simétrica respecto a su diagonal principal

Autor:        Roberto Carlos Iglesias Álvarez
Fecha:        2025-06-14
Estado:       [Terminado]
'''

N = int(input("Ingrese la dimensión de la matriz: "))
matriz = []

print("Ingrese las filas de la matriz, separando los números con comas:")
for i in range(N):
    fila = list(map(int, input(f"Fila {i+1}: ").split(',')))
    while len(fila) != N:
        print("Error: la fila debe tener exactamente", N, "elementos.")
        fila = list(map(int, input(f"Fila {i+1} (nuevamente): ").split(',')))
    matriz.append(fila)

simetrica = True
for i in range(N):
    for j in range(N):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break
    if not simetrica:
        break

if simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
